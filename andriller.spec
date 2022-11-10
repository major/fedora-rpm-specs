Name:           andriller
Version:        3.3.1
Release:        8%{?dist}
Summary:        Android Forensic Tools

License:        MIT
URL:            https://www.andriller.com/
Source0:        https://github.com/den4uk/andriller/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
Patch0:         %{name}-requirements.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-setuptools
BuildRequires:  python3-requests
BuildRequires:  python3-jinja2
BuildRequires:  python3-appdirs
BuildRequires:  python3-javaobj
BuildRequires:  python3-timeout-decorator
BuildRequires:  python3-pycryptodomex
BuildRequires:  python3-xlsxwriter
BuildRequires:  desktop-file-utils

Requires:       android-tools
Requires:       python3-tkinter

%description
Andriller is software utility with a collection of forensic tools for smart 
phones. It performs read-only, forensically sound, non-destructive acquisition
from Android devices. It has features, such as powerful Lockscreen cracking 
for pattern, PIN code or password. Custom decoders for Apps data from Android
(some Apple iOS & Windows) databases for decoding communications. Extraction
and decoders produce reports in HTML and spreadsheet formats.

%prep
%autosetup -p1
# Remove Windows executable
rm -rf andriller/bin
# Remove shebang
sed -i -e '/^#!\//, 1d' andriller/{screencap.py,windows.py}

%build
%py3_build

%install
%py3_install
# Install desktop file
mkdir -p %{buildroot}%{_datadir}/applications/
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
%{__python3} %{_rpmconfigdir}/redhat/pathfix.py -pn -i "%{__python3}" %{buildroot}%{_bindir}/andriller-gui.py

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} pytest-%{python3_version} -v tests

%files
%doc README.md
%license LICENSE
%{_bindir}/andriller-gui.py
%{_datadir}/applications/%{name}.desktop
%{python3_sitelib}/%{name}/
%{python3_sitelib}/*.egg-info/

%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 3.3.1-7
- Rebuilt for Python 3.11

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 3.3.1-4
- Rebuilt for Python 3.10

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Mar 22 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.3.1-1
- Enable tests
- Update to latest upstream release 3.3.1

* Wed Mar 18 2020 Fabian Affolter <mail@fabian-affolter.ch> - 3.3.0-1
- Initial package for Fedora
