%global _with_bootstrap 1
%bcond_with bootstrap

Name:           python-androguard
# Newer versions require Frida which is not yet packaged.
# Currently the main dependency is fdroidserver which uses
# this version
Version:        3.4.0a1
Release:        %autorelease
Summary:        Reverse engineering and pentesting for Android applications

License:        Apache-2.0
URL:            https://github.com/androguard/androguard
# The source release contains binaries with unknown licenses and malware
#OriginalSource: %%{url}/archive/v%%{version}/androguard-%%{version}.tar.gz
Source0:         androguard-%{version}-clean.tar.gz
# script to remov binaries from source code
Source1:         clean.sh

BuildArch:      noarch
BuildRequires:  python3-devel
%if %{without bootstrap}
# Documentation
BuildRequires:  help2man
BuildRequires:  make
BuildRequires:  texinfo
BuildRequires:  python3dist(androguard)
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-sphinxcontrib-programoutput
%endif
# Import check
BuildRequires:  python3-pyperclip
BuildRequires:  python3-qt5
 
%global _description %{expand:
Androguard is a full python tool to play with Android files.
- DEX, ODEX
- APK
- Android's binary xml
- Android resources
- Disassemble DEX/ODEX bytecodes
- Basic Decompiler for DEX/ODEX files
- Frida support for easy dynamic analysis
- SQLite database to save the session}

%description %_description

%package -n     python3-androguard
Summary:        %{summary}

%description -n python3-androguard %_description


%prep
%autosetup -p1 -n androguard-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel
%if %{without bootstrap}
help2man --version-string='%{version}' --no-discard-stderr  --no-info --name='%{summary}' --output=androapkid.1 androapkid
help2man --version-string='%{version}' --no-discard-stderr  --no-info --name='%{summary}' --output=androarsc.1 androarsc
help2man --version-string='%{version}' --no-discard-stderr  --no-info --name='%{summary}' --output=androaxml.1 androaxml
help2man --version-string='%{version}' --no-discard-stderr  --no-info --name='%{summary}' --output=androcg.1 androcg
help2man --version-string='%{version}' --no-discard-stderr  --no-info --name='%{summary}' --output=androdd.1 androdd
help2man --version-string='%{version}' --no-discard-stderr  --no-info --name='%{summary}' --output=androdis.1 androdis
help2man --version-string='%{version}' --no-discard-stderr  --no-info --name='%{summary}' --output=androguard.1 androguard
help2man --version-string='%{version}' --no-discard-stderr  --no-info --name='%{summary}' --output=androlyze.1 androlyze
help2man --version-string='%{version}' --no-discard-stderr  --no-info --name='%{summary}' --output=androsign.1 androsign

pushd docs
make texinfo
pushd build
pushd texinfo
makeinfo --docbook Androguard.texi
popd
popd
popd
%endif

%install
%pyproject_install
%pyproject_save_files -l androguard

%if %{without bootstrap}
mkdir -p %{buildroot}%{_mandir}/man1
install -m644 androapkid.1 %{buildroot}%{_mandir}/man1/
install -m644 androarsc.1 %{buildroot}%{_mandir}/man1/
install -m644 androaxml.1 %{buildroot}%{_mandir}/man1/
install -m644 androcg.1 %{buildroot}%{_mandir}/man1/
install -m644 androdd.1 %{buildroot}%{_mandir}/man1/
install -m644 androdis.1 %{buildroot}%{_mandir}/man1/
install -m644 androguard.1 %{buildroot}%{_mandir}/man1/
install -m644 androlyze.1 %{buildroot}%{_mandir}/man1/
install -m644 androsign.1 %{buildroot}%{_mandir}/man1/

mkdir -p %{buildroot}%{_datadir}/help/en/Androguard
install -m644 docs/build/texinfo/Androguard.xml %{buildroot}%{_datadir}/help/en/Androguard
cp -p -r docs/build/texinfo/Androguard-figures %{buildroot}%{_datadir}/help/en/Androguard/
%endif

%check
%pyproject_check_import

%files -n python3-androguard -f %{pyproject_files}
%{_bindir}/androapkid
%{_bindir}/androarsc
%{_bindir}/androaxml
%{_bindir}/androcg
%{_bindir}/androdd
%{_bindir}/androdis
%{_bindir}/androguard
%{_bindir}/androgui
%{_bindir}/androlyze
%{_bindir}/androsign
%if %{without bootstrap}
%{_mandir}/man1/androapkid.1*
%{_mandir}/man1/androarsc.1*
%{_mandir}/man1/androaxml.1*
%{_mandir}/man1/androcg.1*
%{_mandir}/man1/androdd.1*
%{_mandir}/man1/androdis.1*
%{_mandir}/man1/androguard.1*
%{_mandir}/man1/androlyze.1*
%{_mandir}/man1/androsign.1*
%dir  %{_datadir}/help/en
%lang(en) %{_datadir}/help/en/Androguard
%endif

%changelog
%autochangelog
