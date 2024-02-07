%global srcname selenium

Name:          python-%{srcname}
Version:       4.17.2
Release:       %autorelease
Summary:       Python bindings for Selenium
License:       Apache-2.0
URL:           http://docs.seleniumhq.org/

Source0:       %pypi_source

BuildArch:     noarch

Patch1:        selenium-use-without-bundled-libs.patch

%description
The selenium package is used automate web browser interaction from Python.

Several browsers/drivers are supported (Firefox, Chrome, Internet Explorer,
PhantomJS), as well as the Remote protocol.


%package -n python3-%{srcname}
Summary:       Python bindings for Selenium

BuildRequires: pyproject-rpm-macros
BuildRequires: python3-devel
Requires:      python3-rdflib
BuildArch:     noarch

%description -n python3-%{srcname}
The selenium package is used automate web browser interaction from Python.

Several browsers/drivers are supported (Firefox, Chrome, Internet Explorer,
PhantomJS), as well as the Remote protocol.

%prep
%autosetup -p1 -n %{srcname}-%{version}
find . -type f -name "*.py" -exec sed -i '1{/^#!/d;}' {} \;

%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files %{srcname}
sed -ie '/x_ignore_nofocus.so$/d' %pyproject_files
rm -f %{buildroot}%{python3_sitelib}/selenium/webdriver/firefox/amd64/x_ignore_nofocus.so
rm -f %{buildroot}%{python3_sitelib}/selenium/webdriver/firefox/x86/x_ignore_nofocus.so


%files -n python3-%{srcname} -f %pyproject_files
%license LICENSE
%doc CHANGES README.rst


%changelog
%autochangelog
