# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['DelOsuScript.py', 'utils.py'],
             pathex=['C:\\Users\\v_lijianxun01\\Desktop\\playing\\OSU!曲库谱面删除器'],
             binaries=[],
             datas=[],
             hiddenimports=[],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='OSU!曲库谱面删除器4.0极速版',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True , icon='osu图标.ico')
