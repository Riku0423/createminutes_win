# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['minutes_app.py'],
    pathex=[],
    binaries=[
        ('ffmpeg.exe', '.'),
        ('ffprobe.exe', '.'),
    ],
    datas=[
        ('template.docx', '.'), 
        ('settings.json', '.'),
        ('settings.json', '.'),
    ],
    hiddenimports=[
        'tkinter', 
        'google.generativeai', 
        'openpyxl', 
        'dotenv', 
        'docx'
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='minutes_app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # デバッグ用に一時的にTrue
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    collect_all=['tkinter', 'google.generativeai', 'openpyxl', 'python-dotenv', 'python-docx'],  # 追加
    collect_submodules=['tkinter', 'google.generativeai', 'openpyxl', 'python-dotenv', 'python-docx'],  # 追加
    bundle_identifier=None,
)