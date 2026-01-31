%global giturl  https://github.com/executablebooks/sphinx-book-theme

Name:           python-sphinx-book-theme
Version:        1.1.4
Release:        %autorelease
Summary:        Interactive book theme for Sphinx

License:        BSD-3-Clause
BuildArch:      noarch
URL:            https://jupyterbook.org/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/sphinx-book-theme-%{version}.tar.gz
# Source1 and Source2 created with ./prepare_vendor.sh
Source1:        sphinx-book-theme-%{version}-vendor.tar.xz
Source2:        sphinx-book-theme-%{version}-vendor-licenses.txt
# Compatibility with docutils 0.22.3
Patch:          %{giturl}/pull/919.patch
# Adapt the tests to newer sphinx components
Patch:          %{name}-test.patch

BuildSystem:    pyproject
BuildOption(generate_buildrequires): -x test
BuildOption(install): -L sphinx_book_theme

BuildRequires:  nodejs-devel
BuildRequires:  /usr/bin/node
BuildRequires:  /usr/bin/npm
BuildRequires:  yarnpkg

%global _description %{expand:
This is a lightweight Sphinx theme designed to mimic the look-and-feel of an
interactive book.  It has the following primary features:

- Bootstrap 5 for visual elements and functionality
- Flexible content layout that is inspired by beautiful online books, such as
  the Edward Tufte CSS guide
- Visual classes designed for Jupyter Notebooks.  Cell inputs, outputs, and
  interactive functionality are all supported.
- Launch buttons for online interactivity.  For pages that are built with
  computational material, connect your site to an online BinderHub for
  interactive content.}

%description %_description

%package     -n python3-sphinx-book-theme
Summary:        Interactive book theme for Sphinx

%description -n python3-sphinx-book-theme %_description

%prep
%autosetup -n sphinx-book-theme-%{version} -a1 -p1
cp -p %{SOURCE2} .
rm src/sphinx_book_theme/theme/sphinx_book_theme/static/.gitignore

# Relax strict version requirements
sed -i 's/==/>=/g' pyproject.toml

# Do not run code coverage tests during an RPM build
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#_linters
sed -i '/coverage/d;/pytest-cov/d' pyproject.toml

# Substitute the installed nodejs version for the requested version
%global nodejs_version %(%{_bindir}/node -v | sed s/v//)
sed -i 's,^\(node-version = \)".*",\1"%{nodejs_version}",' pyproject.toml

%build -p
export YARN_CACHE_FOLDER="$PWD/.package-cache"
yarn install --offline
nodeenv --node=system --prebuilt --clean-src $PWD/.nodeenv

%check
%pytest -v

%files -n python3-sphinx-book-theme -f %{pyproject_files}
%doc CHANGELOG.md README.md
%license LICENSE sphinx-book-theme-%{version}-vendor-licenses.txt

%changelog
%autochangelog
