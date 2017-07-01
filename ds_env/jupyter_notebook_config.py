# http://protips.maxmasnick.com/ipython-notebooks-automatically-export-py-and-html
import io
import os
from notebook.utils import to_api_path

_script_exporter = None
_html_exporter = None

def script_post_save(model, os_path, contents_manager, **kwargs):
    """convert notebooks to Python script after save with nbconvert
    replaces `ipython notebook --script`
    """
    from nbconvert.exporters.script import ScriptExporter
    from nbconvert.exporters.html import HTMLExporter

    if model['type'] != 'notebook':
        return

    global _script_exporter
    if _script_exporter is None:
        _script_exporter = ScriptExporter(parent=contents_manager)
    log = contents_manager.log

    global _html_exporter
    if _html_exporter is None:
        _html_exporter = HTMLExporter(parent=contents_manager)
    log = contents_manager.log

    # save .py file
    base, ext = os.path.splitext(os_path)
    script, resources = _script_exporter.from_filename(os_path)
    script_fname = base + resources.get('output_extension', '.txt')
    log.info("Saving script /%s", to_api_path(script_fname, contents_manager.root_dir))
    with io.open(script_fname, 'w', encoding='utf-8') as f:
        f.write(script)

    # save html
    # base, ext = os.path.splitext(os_path)
    # script, resources = _html_exporter.from_filename(os_path)
    # script_fname = base + resources.get('output_extension', '.txt')
    # log.info("Saving html /%s", to_api_path(script_fname, contents_manager.root_dir))
    # with io.open(script_fname, 'w', encoding='utf-8') as f:
    #     f.write(script)
c.FileContentsManager.post_save_hook = script_post_save