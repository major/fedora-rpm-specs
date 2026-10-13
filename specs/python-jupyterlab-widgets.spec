Name:           python-jupyterlab-widgets
Version:        3.0.17
Release:        %autorelease
Summary:        Jupyter interactive widgets for JupyterLab
# JupyterLab widgets themselves are BSD-3-Clause.
# The rest are licenses of bundled JS libs.
#
# [[[cog
#    import cog
#    from glob import glob
#    from pathlib import Path
#    import json
#
#    file = sorted(
#        glob("python-jupyterlab-widgets-*-build/jupyterlab_widgets-*/labextension/static/third-party-licenses.json")
#        )[-1]
#    text = Path(file).read_text()
#    data = json.loads(text)
#    licenses = set([p["licenseId"] for p in data["packages"]])
#    for license in sorted(licenses):
#        cog.outl(f"# {license}")
# ]]]
# BSD-2-Clause
# BSD-3-Clause
# ISC
# MIT
# [[[end]]]
License:        BSD-2-Clause AND BSD-3-Clause AND ISC AND MIT
URL:            https://github.com/jupyter-widgets/ipywidgets
Source:         %{pypi_source jupyterlab_widgets}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python-jupyter-filesystem

%global _description %{expand:
A JupyterLab 3.0 extension for Jupyter/IPython widgets.}

%description %_description

%package -n     python3-jupyterlab-widgets
Summary:        %{summary}

Requires:       python-jupyter-filesystem

# Bundled provides (uses data loaded above)
#
# [[[cog
#    packages = [(p["name"], p["versionInfo"]) for p in data["packages"]]
#    for name, version in sorted(packages):
#        cog.outl(f"Provides:        bundled(npm({name})) = {version}")
# ]]]
Provides:        bundled(npm(@jupyter-widgets/base)) = 6.0.12
Provides:        bundled(npm(@jupyter-widgets/base-manager)) = 1.0.13
Provides:        bundled(npm(@jupyter-widgets/controls)) = 5.0.13
Provides:        bundled(npm(@jupyter-widgets/output)) = 6.0.12
Provides:        bundled(npm(backbone)) = 1.4.0
Provides:        bundled(npm(base64-js)) = 1.5.1
Provides:        bundled(npm(css-loader)) = 6.11.0
Provides:        bundled(npm(d3-color)) = 3.1.0
Provides:        bundled(npm(d3-format)) = 3.1.2
Provides:        bundled(npm(deepmerge)) = 4.3.1
Provides:        bundled(npm(dom-serializer)) = 2.0.0
Provides:        bundled(npm(domelementtype)) = 2.3.0
Provides:        bundled(npm(domhandler)) = 5.0.3
Provides:        bundled(npm(domutils)) = 3.1.0
Provides:        bundled(npm(entities)) = 4.5.0
Provides:        bundled(npm(escape-string-regexp)) = 4.0.0
Provides:        bundled(npm(htmlparser2)) = 8.0.2
Provides:        bundled(npm(is-plain-object)) = 5.0.0
Provides:        bundled(npm(jquery)) = 3.7.1
Provides:        bundled(npm(lodash)) = 4.18.1
Provides:        bundled(npm(nanoid)) = 3.3.18
Provides:        bundled(npm(nouislider)) = 15.4.0
Provides:        bundled(npm(parse-srcset)) = 1.0.2
Provides:        bundled(npm(picocolors)) = 1.1.1
Provides:        bundled(npm(postcss)) = 8.5.26
Provides:        bundled(npm(process)) = 0.11.10
Provides:        bundled(npm(sanitize-html)) = 2.13.1
Provides:        bundled(npm(semver)) = 7.8.5
Provides:        bundled(npm(style-loader)) = 3.3.4
Provides:        bundled(npm(underscore)) = 1.13.7
# [[[end]]]


%description -n python3-jupyterlab-widgets %_description


%prep
%autosetup -p1 -n jupyterlab_widgets-%{version}

# jupyter_builder is not packaged in Fedora; the labextension is pre-built so the hook skips anyway
sed -i 's/, "jupyter_builder>=[^"]*"//' pyproject.toml

# Remove all backup files
find ./ -name "*.json.orig" -delete


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files -l jupyterlab_widgets


%check
%pyproject_check_import


%files -n python3-jupyterlab-widgets -f %{pyproject_files}
%doc README.md
%{_datadir}/jupyter/labextensions/@jupyter-widgets


%changelog
%autochangelog
