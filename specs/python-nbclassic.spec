Name:           python-nbclassic
Version:        1.3.3
Release:        %autorelease
Summary:        Jupyter Notebook as a Jupyter Server Extension

# nbclassic itself is BSD-3-Clause
# The rest are licenses of bundled JS libs.
#
# [[[cog
#    import cog
#    from glob import glob
#    from pathlib import Path
#    import json
#
#    licenses = {}
#    versions = {}
#    not_found_licenses = []
#    not_found_versions = []
#    components = sorted(
#        glob("python-nbclassic-*-build/nbclassic-*/nbclassic/static/components/*"))
#
#    for component in components:
#        for file in ".bower.json", "bower.json", "package.json", "composer.json":
#            path = Path(component) / file
#            name = path.parent.name
#            if path.is_file():
#                data = json.loads(path.read_text())
#                if "license" in data and name not in licenses:
#                    license = data["license"]
#                    if isinstance(license, list):
#                        license = " AND ".join(license)
#                    licenses[name] = license
#
#                if "version" in data and name not in versions:
#                    versions[name] = data["version"]
#        if name not in licenses:
#            not_found_licenses.append(name)
#        if name not in versions:
#            not_found_versions.append(name)
#
#    cog.outl("# Licenses found:")
#    for license in sorted(set(licenses.values())):
#        cog.outl(f"#  - {license}")
#    cog.outl("#\n# License not found for:")
#    for component in sorted(set(not_found_licenses)):
#        cog.outl(f"#  - {component}")
#
# ]]]
# Licenses found:
#  - (OFL-1.1 AND MIT)
#  - Apache 2.0
#  - Apache-2.0
#  - ISC
#  - MIT
#
# License not found for:
#  - create-react-class
#  - sanitizer
#  - text-encoding
#  - xterm.js
#  - xterm.js-css
#  - xterm.js-fit
# [[[end]]]
#
# Manual license detective work:
# - Apache-2.0 - sanitizer
# - MIT - create-react-class, es6-promise, react, requirejs-plugins, xterm

License:        BSD-3-Clause AND Apache-2.0 AND MIT AND (MIT AND OFL-1.1) AND ISC
URL:            https://jupyter.org
Source:         %{pypi_source nbclassic}
# Patch to use the TeX fonts from the MathJax package rather than STIXWeb
# See BZ: 1581899, 1580129
Patch:          Use-MathJax-TeX-fonts-rather-than-STIXWeb.patch

BuildArch:      noarch
BuildRequires:  python3-devel
# Upstream requires "babel" pkg but in Fedora
# python3-babel does not contain "pybabel" tool.
BuildRequires:  babel
# for validating desktop entry
BuildRequires:  desktop-file-utils

%global _description %{expand:
This project prepares for a future where JupyterLab and other
frontends switch to Jupyter Server for their Python Web application
backend. Using this package, users can launch Jupyter NbClassic,
JupyterLab and other frontends side-by-side on top of
the new Python server backend.}


%description %_description

%package -n     python3-nbclassic
Summary:        %{summary}

Requires:       hicolor-icon-theme
Requires:       python-jupyter-filesystem

# Originally bundled fonts
Requires:       font(fontawesome)
%if 0%{?fedora} > 38
Requires:       fontawesome4-fonts-web
%else
Requires:       fontawesome-fonts-web
%endif

# Bundled JS libraries in nbclassic/static/components/ (uses data loaded above)
#
# [[[cog
#    cog.outl("# Version not found for:")
#    for name in sorted(set(not_found_versions)):
#        cog.outl(f"#  - {name}")
#    for name, version in versions.items():
#        cog.outl(f"Provides:        bundled(npm({name})) = {version}")
# ]]]
# Version not found for:
#  - create-react-class
#  - sanitizer
#  - xterm.js
#  - xterm.js-css
#  - xterm.js-fit
Provides:        bundled(npm(MathJax)) = 2.7.9
Provides:        bundled(npm(backbone)) = 1.6.1
Provides:        bundled(npm(bootstrap)) = 3.4.1
Provides:        bundled(npm(bootstrap-tour)) = 0.12.0
Provides:        bundled(npm(codemirror)) = 5.58.3
Provides:        bundled(npm(es6-promise)) = 1.0.0
Provides:        bundled(npm(font-awesome)) = 4.7.0
Provides:        bundled(npm(google-caja-sanitizer)) = 1.0.4
Provides:        bundled(npm(jed)) = 1.1.1
Provides:        bundled(npm(jquery)) = 3.7.1
Provides:        bundled(npm(jquery-typeahead)) = 2.10.7
Provides:        bundled(npm(jquery-ui)) = 1.13.3
Provides:        bundled(npm(marked)) = 4.0.19
Provides:        bundled(npm(moment)) = 2.29.4
Provides:        bundled(npm(react)) = 16.0.0
Provides:        bundled(npm(react-dom)) = 16.0.1
Provides:        bundled(npm(requirejs)) = 2.3.7
Provides:        bundled(npm(requirejs-plugins)) = 1.0.2
Provides:        bundled(npm(requirejs-text)) = 2.0.16
Provides:        bundled(npm(text-encoding)) = 0.1.0
Provides:        bundled(npm(underscore)) = 1.13.7
# [[[end]]]


%description -n python3-nbclassic %_description


%prep
%autosetup -p1 -n nbclassic-%{version}
sed -ri "/(pytest-cov|coverage|nbval|pytest-playwright|pytest-tornasync)/d" pyproject.toml


%generate_buildrequires
%pyproject_buildrequires -x test


%build
%pyproject_wheel


%install
%pyproject_install

# Unbundle fonts
pushd %{buildroot}%{python3_sitelib}/nbclassic/static/components
  rm -r font-awesome/{fonts,css}
  ln -vfs %{_datadir}/fonts/fontawesome font-awesome/fonts
  ln -vfs %{_datadir}/font-awesome-web/css font-awesome/css
popd

install -m 0755 -p -d %{buildroot}%{_sysconfdir}/jupyter/jupyter_server_config.d
mv -v %{buildroot}{%{_prefix},}%{_sysconfdir}/jupyter/jupyter_server_config.d/nbclassic.json

# Remove .po files
rm -v $(find %{buildroot}%{python3_sitelib}/nbclassic/i18n -type f -name '*.po')

# Remove tests
rm -rv $(find %{buildroot}%{python3_sitelib}/nbclassic -type d -name tests)


%check
%pytest

desktop-file-validate %{buildroot}%{_datadir}/applications/jupyter-nbclassic.desktop

# Directory /nbclassic/static/components/font-awesome/css has been symlinked
# to Fedora resources in python3-nbclassic 0.5.4-2.fc39
# causing file conflict when upgrading the package
%if "%{python3_version}" == "3.11"
%pretrans -n python3-nbclassic -p <lua>
path = "%{python3_sitelib}/nbclassic/static/components/font-awesome/css"
st = posix.stat(path)
if st and st.type == "directory" then
  status = os.rename(path, path .. ".rpmmoved")
  if not status then
    suffix = 0
    while not status do
      suffix = suffix + 1
      status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
    end
    os.rename(path, path .. ".rpmmoved")
  end
end
%endif


%files -n python3-nbclassic
%doc README.md
%{_bindir}/jupyter-nbclassic*
%{python3_sitelib}/nbclassic-%{version}.dist-info

# To exclude i18n
%dir %{python3_sitelib}/nbclassic
%{python3_sitelib}/nbclassic/[_a-hj-z]*

# Lang files
%dir %{python3_sitelib}/nbclassic/i18n/
%{python3_sitelib}/nbclassic/i18n/*.py
%{python3_sitelib}/nbclassic/i18n/*.cfg
%{python3_sitelib}/nbclassic/i18n/*.md
%{python3_sitelib}/nbclassic/i18n/*.json
%{python3_sitelib}/nbclassic/i18n/__pycache__/
%lang(fr) %{python3_sitelib}/nbclassic/i18n/fr_FR/
%lang(ja) %{python3_sitelib}/nbclassic/i18n/ja_JP/
%lang(nl) %{python3_sitelib}/nbclassic/i18n/nl/
%lang(ru) %{python3_sitelib}/nbclassic/i18n/ru_RU/
%lang(zh) %{python3_sitelib}/nbclassic/i18n/zh_CN/

# Config and desktop files
%config(noreplace) %{_sysconfdir}/jupyter/jupyter_server_config.d/nbclassic.json
%{_datadir}/applications/jupyter-nbclassic.desktop
%{_datadir}/icons/hicolor/scalable/apps/nbclassic.svg

# A backed-up directory from an older version may be present:
%if "%{python3_version}" == "3.11"
%ghost %{python3_sitelib}/nbclassic/static/components/font-awesome/css.rpmmoved/
%ghost %{python3_sitelib}/nbclassic/static/components/font-awesome/css.rpmmoved/font-awesome.css
%ghost %{python3_sitelib}/nbclassic/static/components/font-awesome/css.rpmmoved/font-awesome.min.css
%endif

%changelog
%autochangelog
