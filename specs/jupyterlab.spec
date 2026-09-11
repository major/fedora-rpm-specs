# Unset -s on python shebang - ensure that extensions installed with pip
# to user locations are seen and properly loaded
%undefine _py3_shebang_s

Name:           jupyterlab
Version:        4.6.3
Release:        %autorelease
Summary:        JupyterLab computational environment
# JupyterLab itself is BSD-3-Clause and
# semver.py file is MIT.
# The rest are licenses of bundled JS libs.
#
# [[[cog
#    import cog
#    from glob import glob
#    from pathlib import Path
#    import json
#
#    file = sorted(
#        glob("jupyterlab-*-build/jupyterlab-*/jupyterlab/static/third-party-licenses.json")
#        )[-1]
#    text = Path(file).read_text()
#    data = json.loads(text)
#    licenses = set([p["licenseId"] for p in data["packages"]])
#    for license in sorted(licenses):
#        cog.outl(f"# {license}")
# ]]]
# 
# (CC-BY-4.0 AND OFL-1.1 AND MIT)
# (MPL-2.0 OR Apache-2.0)
# Apache-2.0
# BSD-2-Clause
# BSD-3-Clause
# EPL-2.0
# ISC
# MIT
# [[[end]]]
License:        Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND (CC-BY-4.0 AND OFL-1.1 AND MIT) AND EPL-2.0 AND ISC AND (MPL-2.0 OR Apache-2.0) AND MIT
URL:            https://jupyter.org
Source0:        %{pypi_source}
# TODO: propose upstream
Source1:        jupyterlab.metainfo.xml

BuildArch:      noarch
BuildRequires:  python3-devel
# Needed for tests
BuildRequires:  nodejs
BuildRequires:  npm
# For validating desktop entry and appdata
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

Requires: python-jupyter-filesystem
Requires: hicolor-icon-theme

# pip allows to install third-party
# extensions into jupyterlab.
Recommends: python3-pip

%py_provides    python3-jupyterlab
%py_provides    jupyter-lab

# Bundled provides (uses data loaded above)
#
# [[[cog
#    packages = [(p["name"], p["versionInfo"]) for p in data["packages"]]
#    for name, version in sorted(packages):
#        cog.outl(f"Provides:        bundled(npm({name})) = {version}")
# ]]]
Provides:        bundled(npm(@braintree/sanitize-url)) = 7.1.1
Provides:        bundled(npm(@codemirror/autocomplete)) = 6.20.0
Provides:        bundled(npm(@codemirror/commands)) = 6.10.2
Provides:        bundled(npm(@codemirror/lang-cpp)) = 6.0.3
Provides:        bundled(npm(@codemirror/lang-css)) = 6.3.1
Provides:        bundled(npm(@codemirror/lang-html)) = 6.4.11
Provides:        bundled(npm(@codemirror/lang-java)) = 6.0.2
Provides:        bundled(npm(@codemirror/lang-javascript)) = 6.2.4
Provides:        bundled(npm(@codemirror/lang-json)) = 6.0.2
Provides:        bundled(npm(@codemirror/lang-markdown)) = 6.5.0
Provides:        bundled(npm(@codemirror/lang-php)) = 6.0.2
Provides:        bundled(npm(@codemirror/lang-python)) = 6.2.1
Provides:        bundled(npm(@codemirror/lang-rust)) = 6.0.2
Provides:        bundled(npm(@codemirror/lang-sql)) = 6.10.0
Provides:        bundled(npm(@codemirror/lang-wast)) = 6.0.2
Provides:        bundled(npm(@codemirror/lang-xml)) = 6.1.0
Provides:        bundled(npm(@codemirror/language)) = 6.12.1
Provides:        bundled(npm(@codemirror/legacy-modes)) = 6.5.2
Provides:        bundled(npm(@codemirror/search)) = 6.6.0
Provides:        bundled(npm(@codemirror/state)) = 6.5.4
Provides:        bundled(npm(@codemirror/view)) = 6.39.14
Provides:        bundled(npm(@fortawesome/fontawesome-free)) = 5.15.4
Provides:        bundled(npm(@jupyter/react-components)) = 0.16.6
Provides:        bundled(npm(@jupyter/web-components)) = 0.16.6
Provides:        bundled(npm(@jupyter/ydoc)) = 4.0.0
Provides:        bundled(npm(@jupyterlab/application)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/application-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/apputils)) = 4.7.3
Provides:        bundled(npm(@jupyterlab/apputils-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/attachments)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/audio-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/cell-toolbar)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/cell-toolbar-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/cells)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/celltags-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/codeeditor)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/codemirror)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/codemirror-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/completer)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/completer-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/console)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/console-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/coreutils)) = 6.6.3
Provides:        bundled(npm(@jupyterlab/csvviewer)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/csvviewer-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/debugger)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/debugger-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/docmanager)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/docmanager-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/docregistry)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/documentsearch)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/documentsearch-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/extensionmanager)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/extensionmanager-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/filebrowser)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/filebrowser-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/fileeditor)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/fileeditor-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/help-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/htmlviewer)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/htmlviewer-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/hub-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/imageviewer)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/imageviewer-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/inspector)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/inspector-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/javascript-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/json-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/launcher)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/launcher-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/logconsole)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/logconsole-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/lsp)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/lsp-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/mainmenu)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/mainmenu-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/markdownviewer)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/markdownviewer-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/markedparser-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/mathjax-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/mermaid)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/mermaid-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/metadataform)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/metadataform-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/nbformat)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/notebook)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/notebook-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/observables)) = 5.6.3
Provides:        bundled(npm(@jupyterlab/outputarea)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/pdf-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/pluginmanager)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/pluginmanager-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/property-inspector)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/rendermime)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/rendermime-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/rendermime-interfaces)) = 3.14.3
Provides:        bundled(npm(@jupyterlab/running)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/running-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/services)) = 7.6.3
Provides:        bundled(npm(@jupyterlab/services-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/settingeditor)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/settingeditor-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/settingregistry)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/shortcuts-extension)) = 5.4.3
Provides:        bundled(npm(@jupyterlab/statedb)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/statusbar)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/statusbar-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/terminal)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/terminal-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/theme-dark-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/theme-dark-high-contrast-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/theme-light-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/toc)) = 6.6.3
Provides:        bundled(npm(@jupyterlab/toc-extension)) = 6.6.3
Provides:        bundled(npm(@jupyterlab/tooltip)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/tooltip-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/translation)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/translation-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/ui-components)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/ui-components-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/vega5-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/video-extension)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/workspaces)) = 4.6.3
Provides:        bundled(npm(@jupyterlab/workspaces-extension)) = 4.6.3
Provides:        bundled(npm(@lezer/common)) = 1.5.0
Provides:        bundled(npm(@lezer/generator)) = 1.7.0
Provides:        bundled(npm(@lezer/highlight)) = 1.2.1
Provides:        bundled(npm(@lezer/lr)) = 1.4.0
Provides:        bundled(npm(@lumino/algorithm)) = 2.0.4
Provides:        bundled(npm(@lumino/application)) = 2.4.9
Provides:        bundled(npm(@lumino/commands)) = 2.3.3
Provides:        bundled(npm(@lumino/coreutils)) = 2.2.2
Provides:        bundled(npm(@lumino/datagrid)) = 2.5.7
Provides:        bundled(npm(@lumino/disposable)) = 2.1.5
Provides:        bundled(npm(@lumino/domutils)) = 2.0.4
Provides:        bundled(npm(@lumino/dragdrop)) = 2.1.8
Provides:        bundled(npm(@lumino/keyboard)) = 2.0.4
Provides:        bundled(npm(@lumino/messaging)) = 2.0.4
Provides:        bundled(npm(@lumino/polling)) = 2.1.5
Provides:        bundled(npm(@lumino/properties)) = 2.0.4
Provides:        bundled(npm(@lumino/signaling)) = 2.1.5
Provides:        bundled(npm(@lumino/virtualdom)) = 2.0.4
Provides:        bundled(npm(@lumino/widgets)) = 2.8.0
Provides:        bundled(npm(@mermaid-js/layout-elk)) = 0.2.1
Provides:        bundled(npm(@mermaid-js/parser)) = 1.1.1
Provides:        bundled(npm(@microsoft/fast-element)) = 1.12.0
Provides:        bundled(npm(@microsoft/fast-foundation)) = 2.49.4
Provides:        bundled(npm(@microsoft/fast-web-utilities)) = 5.4.1
Provides:        bundled(npm(@module-federation/error-codes)) = 2.4.0
Provides:        bundled(npm(@module-federation/runtime)) = 2.4.0
Provides:        bundled(npm(@module-federation/runtime-core)) = 2.4.0
Provides:        bundled(npm(@module-federation/sdk)) = 2.4.0
Provides:        bundled(npm(@module-federation/webpack-bundler-runtime)) = 2.4.0
Provides:        bundled(npm(@rjsf/core)) = 5.14.3
Provides:        bundled(npm(@rjsf/utils)) = 5.14.3
Provides:        bundled(npm(@rjsf/validator-ajv8)) = 5.14.3
Provides:        bundled(npm(@xterm/addon-canvas)) = 0.7.0
Provides:        bundled(npm(@xterm/addon-fit)) = 0.10.0
Provides:        bundled(npm(@xterm/addon-search)) = 0.15.0
Provides:        bundled(npm(@xterm/addon-web-links)) = 0.11.0
Provides:        bundled(npm(@xterm/addon-webgl)) = 0.18.0
Provides:        bundled(npm(@xterm/xterm)) = 5.5.0
Provides:        bundled(npm(ajv)) = 8.17.1
Provides:        bundled(npm(ajv-formats)) = 2.1.1
Provides:        bundled(npm(base16)) = 1.0.0
Provides:        bundled(npm(clone)) = 2.1.2
Provides:        bundled(npm(color)) = 3.2.1
Provides:        bundled(npm(color-convert)) = 1.9.3
Provides:        bundled(npm(color-name)) = 1.1.3
Provides:        bundled(npm(color-string)) = 1.9.1
Provides:        bundled(npm(compute-gcd)) = 1.2.1
Provides:        bundled(npm(compute-lcm)) = 1.1.2
Provides:        bundled(npm(cose-base)) = 2.2.0
Provides:        bundled(npm(crelt)) = 1.0.6
Provides:        bundled(npm(css-loader)) = 6.11.0
Provides:        bundled(npm(cytoscape)) = 3.33.1
Provides:        bundled(npm(cytoscape-cose-bilkent)) = 4.1.0
Provides:        bundled(npm(cytoscape-fcose)) = 2.2.0
Provides:        bundled(npm(d3)) = 7.9.0
Provides:        bundled(npm(d3-array)) = 3.2.4
Provides:        bundled(npm(d3-color)) = 3.1.0
Provides:        bundled(npm(d3-dispatch)) = 3.0.1
Provides:        bundled(npm(d3-format)) = 3.1.0
Provides:        bundled(npm(d3-hierarchy)) = 3.1.2
Provides:        bundled(npm(d3-interpolate)) = 3.0.1
Provides:        bundled(npm(d3-path)) = 3.1.0
Provides:        bundled(npm(d3-scale)) = 4.0.2
Provides:        bundled(npm(d3-scale-chromatic)) = 3.1.0
Provides:        bundled(npm(d3-shape)) = 3.2.0
Provides:        bundled(npm(d3-time)) = 3.1.0
Provides:        bundled(npm(d3-time-format)) = 4.1.0
Provides:        bundled(npm(d3-timer)) = 3.0.1
Provides:        bundled(npm(dagre-d3-es)) = 7.0.14
Provides:        bundled(npm(dayjs)) = 1.11.19
Provides:        bundled(npm(deepmerge)) = 4.3.0
Provides:        bundled(npm(dom-serializer)) = 2.0.0
Provides:        bundled(npm(domelementtype)) = 2.3.0
Provides:        bundled(npm(domhandler)) = 5.0.3
Provides:        bundled(npm(dompurify)) = 3.4.11
Provides:        bundled(npm(domutils)) = 3.2.2
Provides:        bundled(npm(elkjs)) = 0.9.3
Provides:        bundled(npm(entities)) = 4.4.0
Provides:        bundled(npm(es-toolkit)) = 1.46.1
Provides:        bundled(npm(escape-string-regexp)) = 4.0.0
Provides:        bundled(npm(fast-deep-equal)) = 3.1.3
Provides:        bundled(npm(fast-json-stable-stringify)) = 2.1.0
Provides:        bundled(npm(fast-uri)) = 3.1.2
Provides:        bundled(npm(free-style)) = 3.1.0
Provides:        bundled(npm(htmlparser2)) = 8.0.1
Provides:        bundled(npm(internmap)) = 1.0.1
Provides:        bundled(npm(is-arrayish)) = 0.3.2
Provides:        bundled(npm(is-plain-object)) = 5.0.0
Provides:        bundled(npm(json-schema-compare)) = 0.2.2
Provides:        bundled(npm(json-schema-merge-allof)) = 0.8.1
Provides:        bundled(npm(json-schema-traverse)) = 1.0.0
Provides:        bundled(npm(json-stringify-pretty-compact)) = 3.0.0
Provides:        bundled(npm(json5)) = 2.2.3
Provides:        bundled(npm(jsonpointer)) = 5.0.1
Provides:        bundled(npm(katex)) = 0.16.38
Provides:        bundled(npm(khroma)) = 2.1.0
Provides:        bundled(npm(layout-base)) = 2.0.1
Provides:        bundled(npm(lib0)) = 0.2.65
Provides:        bundled(npm(lodash)) = 4.17.21
Provides:        bundled(npm(lodash-es)) = 4.18.1
Provides:        bundled(npm(lodash.curry)) = 4.1.1
Provides:        bundled(npm(lodash.escape)) = 4.0.1
Provides:        bundled(npm(lodash.mergewith)) = 4.6.2
Provides:        bundled(npm(marked)) = 16.4.2
Provides:        bundled(npm(marked-gfm-heading-id)) = 4.1.4
Provides:        bundled(npm(marked-mangle)) = 1.1.13
Provides:        bundled(npm(mathjax-full)) = 3.2.2
Provides:        bundled(npm(mermaid)) = 11.15.0
Provides:        bundled(npm(mhchemparser)) = 4.1.1
Provides:        bundled(npm(minimist)) = 1.2.8
Provides:        bundled(npm(nanoid)) = 3.3.11
Provides:        bundled(npm(parse-srcset)) = 1.0.2
Provides:        bundled(npm(path-browserify)) = 1.0.1
Provides:        bundled(npm(picocolors)) = 1.1.1
Provides:        bundled(npm(postcss)) = 8.5.14
Provides:        bundled(npm(process)) = 0.11.10
Provides:        bundled(npm(querystringify)) = 2.2.0
Provides:        bundled(npm(react)) = 18.2.0
Provides:        bundled(npm(react-dom)) = 18.2.0
Provides:        bundled(npm(react-highlight-words)) = 0.20.0
Provides:        bundled(npm(react-is)) = 18.2.0
Provides:        bundled(npm(react-json-tree)) = 0.18.0
Provides:        bundled(npm(react-paginate)) = 6.5.0
Provides:        bundled(npm(react-toastify)) = 9.1.1
Provides:        bundled(npm(regexp-match-indices)) = 1.0.2
Provides:        bundled(npm(regexp-tree)) = 0.1.24
Provides:        bundled(npm(requires-port)) = 1.0.0
Provides:        bundled(npm(roughjs)) = 4.6.6
Provides:        bundled(npm(sanitize-html)) = 2.12.1
Provides:        bundled(npm(scheduler)) = 0.23.0
Provides:        bundled(npm(semver)) = 7.7.3
Provides:        bundled(npm(simple-swizzle)) = 0.2.2
Provides:        bundled(npm(style-loader)) = 3.3.4
Provides:        bundled(npm(style-mod)) = 4.1.2
Provides:        bundled(npm(tabbable)) = 5.3.3
Provides:        bundled(npm(ts-dedent)) = 2.2.0
Provides:        bundled(npm(typestyle)) = 2.4.0
Provides:        bundled(npm(url-parse)) = 1.5.10
Provides:        bundled(npm(validate.io-array)) = 1.0.6
Provides:        bundled(npm(validate.io-function)) = 1.0.2
Provides:        bundled(npm(validate.io-integer)) = 1.0.5
Provides:        bundled(npm(validate.io-integer-array)) = 1.0.0
Provides:        bundled(npm(validate.io-number)) = 1.0.3
Provides:        bundled(npm(vega)) = 5.33.0
Provides:        bundled(npm(vega-embed)) = 6.21.3
Provides:        bundled(npm(vega-event-selector)) = 3.0.1
Provides:        bundled(npm(vega-lite)) = 5.6.1
Provides:        bundled(npm(vega-util)) = 1.17.4
Provides:        bundled(npm(vscode-jsonrpc)) = 8.2.0
Provides:        bundled(npm(vscode-ws-jsonrpc)) = 1.0.2
Provides:        bundled(npm(yjs)) = 13.5.49
# [[[end]]]


%description
JupyterLab is the next-generation user interface for Project Jupyter
offering all the familiar building blocks of the classic Jupyter
Notebook (notebook, terminal, text editor, file browser, rich outputs, etc.)
in a flexible and powerful user interface.


%prep
%autosetup -p1 -n jupyterlab-%{version}

# pytest-tornasync is not available in Fedora
# and upstream will switch to pytest-jupyter soon
# https://github.com/jupyterlab/jupyterlab/issues/13794
sed -i "/pytest-tornasync/d" pyproject.toml

sed -i "/coverage/d" pyproject.toml
sed -i "/pytest-cov/d" pyproject.toml
sed -i "/pytest-check-links/d" pyproject.toml

# Remove woff and woff2 fonts
find jupyterlab/static -name "*.woff" -delete
find jupyterlab/static -name "*.woff2" -delete

# Remove all empty files
find ./ -empty -type f -delete

# Remove all backup files
find ./ -name "*.json.orig" -delete


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files jupyterlab

# jupyter-labhub requires jupyterhub, which is not available in Fedora
rm %{buildroot}%{_bindir}/jupyter-labhub

# Add %%license to some bundled LICENSE.txt files
sed -i "s/\(.*\.LICEN[SC]E\.txt\)/%%license \1/" %{pyproject_files}

install -m 0755 -p -d %{buildroot}%{_sysconfdir}/jupyter/jupyter_notebook_config.d
install -m 0755 -p -d %{buildroot}%{_sysconfdir}/jupyter/jupyter_server_config.d
mv -v %{buildroot}{%{_prefix},}%{_sysconfdir}/jupyter/jupyter_notebook_config.d/jupyterlab.json
mv -v %{buildroot}{%{_prefix},}%{_sysconfdir}/jupyter/jupyter_server_config.d/jupyterlab.json

# Replace identical files with a symlink
pushd %{buildroot}%{python3_sitelib}/jupyterlab/tests/mock_packages
ln -sf ../../extension/mock_package.py interop/consumer/jlab_mock_consumer.py
popd

# Install appdata
mkdir -p %{buildroot}%{_metainfodir}
install -m 0644 -p %{SOURCE1} %{buildroot}%{_metainfodir}/jupyterlab.metainfo.xml


%check
# Some tests fail because of missing tornasync and
# some try to install dependencies from internet via npm.
# test_load_extension is flaky.
%pytest -k "not test_build and not test_check and not test_install_and_uninstall and not test_uninstall_core_extension and not test_load_extension"

desktop-file-validate %{buildroot}%{_datadir}/applications/jupyterlab.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

# Regression test for node shebang in executable files
grep -E '!#.+node' $(find %{buildroot} -type f -executable) && exit 1 || true


%files -f %{pyproject_files}
%doc README.md
%config(noreplace) %{_sysconfdir}/jupyter/jupyter_notebook_config.d/jupyterlab.json
%config(noreplace) %{_sysconfdir}/jupyter/jupyter_server_config.d/jupyterlab.json
%{_bindir}/jupyter-lab
%{_bindir}/jupyter-labextension
%{_datadir}/jupyter/lab
%{_datadir}/applications/jupyterlab.desktop
%{_datadir}/icons/hicolor/scalable/apps/jupyterlab.svg
%{_metainfodir}/jupyterlab.metainfo.xml


%changelog
%autochangelog
