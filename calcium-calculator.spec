%global tarname calc

Name:       calcium-calculator
Version:    7.9.5
Release:    9%{?dist}
Summary:    The Calcium Calculator

License:    GPLv3+
URL:        https://web.njit.edu/~matveev/calc.html
Source0:    https://web.njit.edu/~matveev/calc/versions/calc_unix_%{version}.tgz
# Sent upstream
Patch0:     0002-Fix-invalid-conversion-from-char-to-char.patch
Patch1:     0003-Include-build-flags.patch
Patch2:     0004-Fix-format-security-issues.patch

BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires: make

%description
CalC ("Calcium Calculator") is a free (GNU copyleft) modeling tool for
simulating intracellular calcium diffusion and buffering. CalC solves
continuous reaction-diffusion PDEs describing the entry of calcium into a
volume through point-like channels, and its diffusion, buffering and binding to
calcium receptors.


%prep
%autosetup -c -n %{name}-%{version} -S git

sed -i 's/\r$//' README.txt
# Remove executable bits
chmod 0644 README.txt

find . -name "*" -type f -exec chmod 0644 '{}' \;
find . -name "*" -type f -exec sed -i 's/\r$//' '{}' \;

%build
%{set_build_flags}
%make_build

%install
# Rename to prevent conflict
mv -v calc %{name}
install -p -m 755 -D -t $RPM_BUILD_ROOT/%{_bindir} %{name}


%files
%doc README.txt examples
%{_bindir}/%{name}

%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.9.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 7.9.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.9.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 7.9.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.9.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 7.9.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 09 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.9.5-3
- Rename binary to prevent conflict with calc: 1781235

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 7.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 19 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 7.9.5-1
- Initial package
