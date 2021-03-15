# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['cli.py'],
             pathex=['C:\\Users\\poeri\\Documenti\\CODING+\\FARMA_PY_EXE'],
             binaries=[],
             datas=[('C:\\Users\\poeri\\Documenti\\CODING+\\FARMA_PY_EXE\\README.md', '.')],
             hiddenimports=['C:\\Users\\poeri\\Documenti\\CODING+\\FARMA_PY_EXE\\db_funcs', 'sqlite3', 'sqlite3.Error'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='FARMA_PY_v01',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='cli')
