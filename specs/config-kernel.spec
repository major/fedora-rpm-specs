
%global commit d696f1609852254038f208c0d163abb39976a57e
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           config-kernel
Version:        0.3
Release:        4%{?dist}
Summary:        An easy way to edit kernel configuration files and templates

License:        GPL-2.0-or-later
URL:            https://github.com/pjps/config-kernel
Source0:        %{URL}/archive/refs/tags/%{name}-%{version}.tar.gz

BuildRequires:  bison
BuildRequires:  bison-devel
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  make


%description
config-kernel tool helps to edit kernel configuration files and templates.
User can query, enable, disable or toggle CONFIG options via command line
switch or an $EDITOR program, without worrying about option dependencies.

%prep
%autosetup -n %{name}-%{version}

%build
CFLAGS="${CFLAGS} -g -fPIE -pie" \
%make_build %{?_smp_mlags}

%check
./configk -h > /dev/null
./configk -v

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man1
install -m 0755 configk %{buildroot}/%{_bindir}/
install -m 0644 configk.1 %{buildroot}/%{_mandir}/man1/


%files
%doc README.md
%license COPYING
%{_bindir}/configk
%{_mandir}/man1/configk.1.gz


%changelog
* Wed Jul 23 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_43_Mass_Rebuild

* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Feb 17 2024 pjp <pjp@fedoraproject.org> - 0.3-1
- New release v0.3

* Fri Feb 09 2024 pjp <pjp@fedoraproject.org> - 0.2^1a9b278-4
- Add "-fPIE -pie" to CFLAGS to make pie executable
- Remove linkage to -lfl to avoid rpmlint(1) warning

* Tue Feb 06 2024 pjp <pjp@fedoraproject.org> - 0.2^18b6853-3
- Fix compiler warnings and install a user manual
- Revise spec file as per review comments BZ#2259602

* Wed Jan 31 2024 pjp <pjp@fedoraproject.org> - 0.2-2
- Update spec file as per review comments BZ#2259602

* Wed Jan 10 2024 pjp <pjp@fedoraproject.org> - 0.2-1
- Initial config-kernel package
