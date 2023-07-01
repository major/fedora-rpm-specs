Name:           python-furo
Version:        2023.03.27
Release:        2%{?dist}
Summary:        Clean customizable Sphinx documentation theme

License:        MIT
URL:            https://pradyunsg.me/furo/
Source0:        https://github.com/pradyunsg/furo/archive/%{version}/furo-%{version}.tar.gz
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
# - _static/basic.css: BSD-2-Clause
# - _static/clipboard.min.js: MIT
# - _static/copy*: MIT
# - _static/doctools.js: BSD-2-Clause
# - _static/jquery*.js: MIT
# - _static/language_data.js: BSD-2-Clause
# - _static/pygments.css: BSD-2-Clause
# - _static/searchtools.js: BSD-2-Clause
# - _static/underscore*.js: MIT
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
%pyproject_save_files furo

# Build documentation
PYTHONPATH=%{buildroot}%{python3_sitelib} sphinx-build -b html docs html
rm -rf html/{.buildinfo,.doctrees}

%check
# There aren't any tests.  When there are, do this:
#%%pytest
%pyproject_check_import

%files -n python3-furo -f %{pyproject_files}
%doc README.md
%license LICENSE

%files doc
%doc html
%license LICENSE

%changelog
* Thu Jun 29 2023 Python Maint <python-maint@redhat.com> - 2023.03.27-2
- Rebuilt for Python 3.12

* Tue Mar 28 2023 Jerry James <loganjerry@gmail.com> - 2023.03.27-1
- Version 2023.03.27

* Thu Feb 23 2023 Jerry James <loganjerry@gmail.com> - 2022.12.07-2
- Dynamically generate BuildRequires
- The node header tarball is no longer needed

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2022.12.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Dec 13 2022 Jerry James <loganjerry@gmail.com> - 2022.12.07-1
- Version 2022.12.07

* Fri Sep 30 2022 Jerry James <loganjerry@gmail.com> - 2022.09.29-1
- Version 2022.09.29

* Thu Aug 25 2022 Jerry James <loganjerry@gmail.com> - 2022.06.21-1
- Initial RPM
