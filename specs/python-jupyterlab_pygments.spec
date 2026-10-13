# Created by pyp2rpm-3.3.5
%global pypi_name jupyterlab_pygments

Name:           python-%{pypi_name}
Version:        0.3.0
Release:        %autorelease
Summary:        Pygments theme
# jupyterlab_pygments itself is BSD-3-Clause.
# The rest are licenses of bundled JS libs.
#
# [[[cog
#    import cog
#    from glob import glob
#    from pathlib import Path
#    import json
#
#    file = sorted(
#        glob("python-jupyterlab_pygments-*-build/jupyterlab_pygments-*/jupyterlab_pygments/labextension/static/third-party-licenses.json")
#        )[-1]
#    text = Path(file).read_text()
#    data = json.loads(text)
#    licenses = set([p["licenseId"] for p in data["packages"]])
#    for license in sorted(licenses):
#        cog.outl(f"# {license}")
# ]]]
# MIT
# [[[end]]]
License:        BSD-3-Clause AND MIT
URL:            https://github.com/jupyterlab/jupyterlab_pygments
Source0:        %{pypi_source}
Patch:          drop-hatch-nodejs-version.patch

BuildArch:      noarch

BuildRequires:  python3-devel

%description
This package contains a syntax coloring theme for pygments making use of the 
JupyterLab CSS variables.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       (python3dist(pygments) >= 2.4.1 with python3dist(pygments) < 3)

# Bundled provides (uses data loaded above)
#
# [[[cog
#    packages = [(p["name"], p["versionInfo"]) for p in data["packages"]]
#    for name, version in sorted(packages):
#        cog.outl(f"Provides:        bundled(npm({name})) = {version}")
# ]]]
Provides:        bundled(npm(css-loader)) = 6.8.1
Provides:        bundled(npm(style-loader)) = 3.3.3
# [[[end]]]

%description -n python3-%{pypi_name}
This package contains a syntax coloring theme for pygments making use of the 
JupyterLab CSS variables.



%prep
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
# Replace dynamic version
sed -i "s/##VERSION##/%{version}/" pyproject.toml
# Remove the build-time dependency on jupyterlab - it's only needed if
# node.js packages are installed during the build, which is not the case in Fedora
sed -i '/"jupyterlab[><"]/d' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_datadir}/jupyter/labextensions/jupyterlab_pygments

%changelog
%autochangelog
