%bcond_with bootstrap

Name:           python-apkinspector
# Get version from GitHub to build documentation
# Latest release on GitHub is behind latest release on PyPI
# https://github.com/erev0s/apkInspector/issues/40
Version:        1.3.2
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        apkInspector is a tool to help examine APK files

License:        Apache-2.0
URL:            https://github.com/erev0s/apkInspector
Source0:        apkInspector-%{version}-clean.tar.gz
# Script to download source and remove binary apks
Source1:        getclean.sh
# Use theme that does not have javascript
Patch:          doc.patch

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{without bootstrap}
BuildRequires:  python3dist(apkinspector)
BuildRequires:  help2man
%endif
# Documentation
BuildRequires:  python3dist(sphinx)
# Use lv_2 instead instead of book-theme
BuildRequires:  python3-sphinx_lv2_theme

%global _description %{expand:
apkInspector is a tool designed to provide detailed insights into the zip
structure of APK files, offering the capability to extract content and decode
the AndroidManifest.xml file. What sets APKInspector apart is its adherence to
the zip specification during APK parsing, eliminating the need for reliance on
external libraries. This independence, allows APKInspector to be highly
adaptable, effectively emulating Android's installation process for APKs that
cannot be parsed using standard libraries. The main goal is to enable users to
conduct static analysis on APKs that employ evasion techniques, especially when
conventional methods prove ineffective.}

%description %_description

%package -n     python3-apkinspector
Summary:        %{summary}

%description -n python3-apkinspector %_description

%package doc
Summary: %{summary}
BuildArch:  noarch

%description doc
Html documentation for apkInspector.

%prep
%autosetup -p1 -n apkInspector-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
%if %{without bootstrap}
help2man --version-string='%{version}' --no-discard-stderr  --no-info --name='%{summary}' --output=apkInspector.1 apkInspector
%endif
pushd docs
sphinx-build _src html -b html
# remove build uneeded artifacts
rm -rf html/.buildinfo
rm -rf html/.doctrees
popd

%install
%pyproject_install
%pyproject_save_files -L apkInspector apkInspectorCLI
%if %{without bootstrap}
mkdir -p %{buildroot}%{_mandir}/man1/
install -m644 apkInspector.1 %{buildroot}%{_mandir}/man1/
%endif

%check
%pyproject_check_import
# Test require packaging binary apks, so not run as these are removed

%files -n python3-apkinspector -f %{pyproject_files}
%{_bindir}/apkInspector
%license LICENSE
%if %{without bootstrap}
%{_mandir}/man1/apkInspector.1*
%endif

%files doc
%license LICENSE
%doc docs/html/

%changelog
%autochangelog
