Name:           python-nbclassic
Version:        1.2.0
Release:        %autorelease
Summary:        Jupyter Notebook as a Jupyter Server Extension

# Main package is BSD-3-Clause
#
# Licenses of the bundled JS libs (semi-automatic)
# helpful cmd: find ./ -name ".bower.json" -or -name "bower.json" -or -name "component.json" -or -name "composer.json" | \
#    xargs grep -i 'license' | sed -r 's/.*components\/(.*)\/.* "(.*)",?/\1: \2/' | sort | uniq | sort
# backbone: MIT
# bootstrap: MIT
# google-caja: Apache 2.0
# jquery: MIT
# jquery-typeahead: MIT
# jquery-ui: MIT
# marked: MIT
# MathJax: Apache-2.0
# moment: MIT
# requirejs-text: MIT
# text-encoding: Apache-2.0
# 
# and the manual detective work:
#
# bootstrap-tour: Apache-2.0
# codemirror: MIT
# es6-promise: MIT (from npmjs.com)
# jed: MIT
# react: MIT
# requirejs{,-plugins,-text}: MIT
# underscore: MIT
#
# to open npm page for bundled JS libs run:
#   find ./ -name ".bower.json" | xargs grep '"version":' | \ 
#   sed -r 's@.*components/(.*)/\.bower\.json: +"version": +"(.*)",@https://www.npmjs.com/package/\1/v/\2@'

License:        BSD-3-Clause AND MIT AND Apache-2.0
URL:            https://jupyter.org
Source:         %{pypi_source nbclassic}
# Patch to use the TeX fonts from the MathJax package rather than STIXWeb
# See BZ: 1581899, 1580129
Patch:          Use-MathJax-TeX-fonts-rather-than-STIXWeb.patch

BuildArch:      noarch
BuildRequires:  python3-devel
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

# Bundled JS libraries in nbclassic/static/components/
# generated in unpacked sources by:
# find ./ -name ".bower.json" | xargs grep '"version":' | sed -r 's/.*components\/(.*)\/\.bower\.json: +"version": +"(.*)",/Provides:        bundled(\1) = \2/' | sort
Provides:        bundled(backbone) = 1.2.0
Provides:        bundled(bootstrap) = 3.4.1
Provides:        bundled(bootstrap-tour) = 0.9.0
Provides:        bundled(codemirror) = 5.58.2
Provides:        bundled(es6-promise) = 1.0.0
Provides:        bundled(google-caja) = 5669.0.0
Provides:        bundled(jed) = 1.1.1
Provides:        bundled(jquery) = 3.5.1
Provides:        bundled(jquery-typeahead) = 2.10.7
Provides:        bundled(jquery-ui) = 1.13.2
Provides:        bundled(marked) = 4.0.19
Provides:        bundled(MathJax) = 2.7.9
Provides:        bundled(moment) = 2.29.4
Provides:        bundled(react) = 16.0.0
Provides:        bundled(requirejs) = 2.2.0
Provides:        bundled(requirejs-plugins) = 1.0.3
Provides:        bundled(requirejs-text) = 2.0.16
Provides:        bundled(text-encoding) = 0.1.0
Provides:        bundled(underscore) = 1.13.6

%description -n python3-nbclassic %_description


%prep
%autosetup -p1 -n nbclassic-%{version}
sed -ri "/(pytest-cov|coverage|nbval|pytest-playwright|pytest_tornasync)/d" setup.cfg
sed -ri "s/'(pytest-cov|coverage|nbval|pytest-playwright|pytest_tornasync)',?//g" setup.py


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
