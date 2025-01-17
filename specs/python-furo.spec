%global giturl  https://github.com/pradyunsg/furo

Name:           python-furo
Version:        2024.08.06
Release:        %autorelease
Summary:        Clean customizable Sphinx documentation theme

License:        MIT
URL:            https://pradyunsg.me/furo/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/%{version}/furo-%{version}.tar.gz
# Source1 and Source2 created with ./prepare_vendor.sh
Source1:        furo-%{version}-vendor.tar.xz
Source2:        furo-%{version}-vendor-licenses.txt

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  nodejs-devel
BuildRequires:  nodejs-npm
BuildRequires:  python-sphinx-doc
BuildRequires:  python3-devel
BuildRequires:  python3-docs
BuildRequires:  yarnpkg

%global _description %{expand:
Furo is a Sphinx theme, which is:
- Intentionally minimal --- the most important thing is the content, not
  the scaffolding around it.
- Responsive --- adapting perfectly to the available screen space, to
  work on all sorts of devices.
- Customizable --- change the color palette, font families, logo and
  more!
- Easy to navigate --- with carefully-designed sidebar navigation and
  inter-page links.
- Good looking content --- through clear typography and well-stylized
  elements.
- Good looking search --- helps readers find what they want quickly.
- Biased for smaller docsets --- intended for smaller documentation
  sets, where presenting the entire hierarchy in the sidebar is not
  overwhelming.}

%description %_description

%package     -n python3-furo
Summary:        Clean customizable Sphinx documentation theme

%description -n python3-furo %_description

%package        doc
Summary:        Documentation for %{name}
# This project is MIT.  Other files bundled with the documentation have the
# following licenses:
# - searchindex.js: BSD-2-Clause
# - _sources/kitchen-sink/*.rst.txt: CC-BY-SA-4.0
# - _sphinx_design_static/*: MIT
# - _static/basic.css: BSD-2-Clause
# - _static/check-solid.svg: MIT
# - _static/clipboard.min.js: MIT
# - _static/copy*: MIT
# - _static/debug.css: MIT
# - _static/demo*.png: MIT
# - _static/design*: MIT
# - _static/doctools.js: BSD-2-Clause
# - _static/file.png: BSD-2-Clause
# - _static/language_data.js: BSD-2-Clause
# - _static/minus.png: BSD-2-Clause
# - _static/pied-piper-admonition.css: MIT
# - _static/plus.png: BSD-2-Clause
# - _static/pygments.css: BSD-2-Clause
# - _static/readthedocs-dummy.js: MIT
# - _static/searchtools.js: BSD-2-Clause
# - _static/skeleton.css: MIT
# - _static/sphinx-design.min.css: MIT
# - _static/sphinx_highlight.js: BSD-2-Clause
# - _static/tabs.*: MIT
License:        MIT AND BSD-2-Clause AND CC-BY-SA-4.0

%description    doc
Documentation for %{name}.

%prep
%autosetup -n furo-%{version} -a1
cp -p %{SOURCE2} .

# Don't ship version control files
find . -name .gitignore -delete

# Substitute the installed nodejs version for the requested version
sed -i 's,^\(node-version = \)".*",\1"%{nodejs_version}",' pyproject.toml

# Use local objects.inv for intersphinx
sed -e 's|\("https://docs\.python\.org/3", \)None|\1"%{_docdir}/python3-docs/html/objects.inv"|' \
    -e 's|\("https://www\.sphinx-doc\.org/en/master", \)None|\1"%{_docdir}/python-sphinx-doc/html/objects.inv"|' \
    -i docs/conf.py

%generate_buildrequires
%pyproject_buildrequires docs/requirements.txt

%build
export PUPPETEER_SKIP_CHROMIUM_DOWNLOAD=1
export YARN_CACHE_FOLDER="$PWD/.package-cache"
yarn install --offline
nodeenv --node=system --prebuilt --clean-src $PWD/.nodeenv

%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L furo

# Build documentation
%{py3_test_envvars} sphinx-build -b html docs html
rm -rf html/{.buildinfo,.doctrees}

%check
# The tests require web access.  If any tests show up that can be run without a
# network, do this:
#%%pytest -v
%pyproject_check_import

%files -n python3-furo -f %{pyproject_files}
%doc README.md
%license LICENSE

%files doc
%doc html
%license LICENSE

%changelog
%autochangelog
