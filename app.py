import os
import ast
import signal
import subprocess
from flask import Flask, request, render_template, jsonify, send_from_directory

app = Flask(__name__)
# Sabhi chalne wale bots ki list rakhne ke liye
active_bots = {}

# Material Scanner Engine
class MaterialIntelligence:
    @staticmethod
    def analyze(file_path):
        try:
            with open(file_path, "r") as f:
                content = f.read()
                tree = ast.parse(content)
            
            # 1. 'Material' ka weight check karo
            nodes = list(ast.walk(tree))
            functions = [n.name for n in nodes if isinstance(n, ast.FunctionDef)]
            imports = []
            for node in nodes:
                if isinstance(node, ast.Import):
                    for n in node.names: imports.append(n.name)
                elif isinstance(node, ast.ImportFrom):
                    imports.append(node.module)

            # 2. Logic Detectors (Intelligent Check)
            has_buttons = "InlineKeyboardMarkup" in content or "ReplyKeyboardMarkup" in content
            is_heavy = "threading" in content or "multiprocessing" in content
            is_unsafe = "attack" in content.lower() or "spam" in content.lower()

            # 3. Intelligent Verdict (Faisla)
            if is_unsafe:
                verdict = "⚠️ CRITICAL: Unsafe Material Detected"
                mode = "Isolated High-Security Mode"
            elif has_buttons:
                verdict = "🎨 UI-Rich: Interactive Bot Detected"
                mode = "User-Interface Optimized"
            elif is_heavy:
                verdict = "⚙️ HEAVY: High Resource Material"
                mode = "Performance Boost Mode"
            else:
                verdict = "✅ STANDARD: Normal Script Detected"
                mode = "Economy Mode"

            return {
                "verdict": verdict,
                "mode": mode,
                "libraries": list(set(imports)) if imports else ["Standard"],
                "complexity": len(functions),
                "safe": not is_unsafe
            }
        except Exception as e:
            return {"verdict": f"Error Scanning: {str(e)}", "mode": "Blocked", "complexity": 0, "safe": False}

@app.route('/')
def index():
    return render_template('index.html', bots=active_bots)

# static folder se image serve karne ke liye route
@app.route('/static/logo.png')
def serve_logo():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'logo.png')

@app.route('/deploy', methods=['POST'])
def deploy():
    token = request.form.get('token')
    admin_id = request.form.get('admin')
    file = request.files.get('file')

    if not token or not admin_id or not file:
        return jsonify({"status": "error", "msg": "Saari details bhariye!"})

    filename = file.filename
    file_path = os.path.join(os.getcwd(), filename)
    file.save(file_path)

    # --- INTELLIGENT SCANNING ---
    intel = MaterialIntelligence.analyze(file_path)
    
    if not intel['safe']:
        os.remove(file_path) # Delete unsafe file
        return jsonify({"status": "error", "msg": "Malicious material blocked!", "intel": intel})

    # --- INJECTION ---
    # File ke andar Token aur ID inject karo
    with open(file_path, 'r') as f:
        code = f.read()
    
    code = code.replace('YOUR_BOT_TOKEN', token).replace('YOUR_ADMIN_ID', admin_id)
    
    with open(file_path, 'w') as f:
        f.write(code)

    # --- DEPLOYMENT ---
    # Agar ye file pehle se chal rahi hai toh use pehle band karo
    if filename in active_bots:
        try:
            os.kill(active_bots[filename]['pid'], signal.SIGTERM)
        except:
            pass

    # Naya process start karo aur use intelligent data ke saath save karo
    try:
        process = subprocess.Popen(["python3", file_path])
        active_bots[filename] = {
            "pid": process.pid,
            "intel": intel,
            "status": "Running",
            "uptime": "Active"
        } 
        return jsonify({"status": "success", "msg": f"{filename} Scanned & Deployed!", "intel": intel})
    except Exception as e:
        return jsonify({"status": "error", "msg": str(e)})

@app.route('/stop/<filename>')
def stop_bot(filename):
    if filename in active_bots:
        try:
            os.kill(active_bots[filename]['pid'], signal.SIGTERM)
            del active_bots[filename]
            return jsonify({"status": "success", "msg": f"Stopped {filename}"})
        except:
            return jsonify({"status": "error", "msg": "Failed to stop"})
    return jsonify({"status": "error", "msg": "Not found"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
