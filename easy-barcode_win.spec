# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_data_files

_easy_barcode_res_files = collect_data_files('easy_barcode')
_pyguiadapter_res_files = collect_data_files('pyguiadapter')

_executable_name = 'easy-barcode-win'
_executable_icon = 'easy_barcode/res/icon.ico'
_main_file = 'easy_barcode/main.py'

a = Analysis(
    [_main_file],
    pathex=[],
    binaries=[],
    datas=[*_easy_barcode_res_files, *_pyguiadapter_res_files],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name=_executable_name,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=[_executable_icon],
)