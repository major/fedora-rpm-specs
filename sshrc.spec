Name:		sshrc
Version:	0.6.2
Release:	9%{?dist}
Summary:	Bring your bash and vim configuration in your ssh session

License:	MIT
URL:		https://github.com/Russell91/sshrc
Source0:	https://github.com/Russell91/sshrc/archive/0.6.2.tar.gz

Requires:	vim-common
Requires:	openssh-clients

BuildArch:	noarch

Provides:	moshrc = %{version}-%{release}

%description
You can use this to set environment variables, define functions,
and run post-login commands. This is quite useful when you have several
servers that you don't want to configure independently.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_bindir}/
cp -p sshrc %{buildroot}/%{_bindir}
cp -p moshrc %{buildroot}/%{_bindir}

%files
%license LICENSE
%doc README.md
%{_bindir}/sshrc
%{_bindir}/moshrc

%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Dec 22 2018 Pranav Kant <pranvk@fedoraproject.org> - 0.6.2-1
- Update to 0.6.2

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 05 2017 Pranav Kant <pranvk@fedoraproject.org> - 0.6.1-1
- Update to 0.6.1

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 8 2015 Pranav Kant <pranvk@fedoraproject.org> - 0.5-5
- Changed Summary: Removed dots "." from it

* Mon Sep 28 2015 Pranav Kant <pranvk@fedoraproject.org> - 0.5-4
- Add moshrc to 'Provides:' field

* Wed Aug 12 2015 Pranav Kant <pranvk@fedoraproject.org> - 0.5-3
- Patch programs to avoid possible accidents

* Sat Aug 1 2015 Pranav Kant <pranvk@fedoraproject.org> - 0.5-2
- Add %%build section to silent rpmlint warning
- Add needed to 'Requires:' field
- Remove 'rm -rf %%buildroot'

* Mon Jul 27 2015 Pranav Kant <pranvk@fedoraproject.org> - 0.5-1
- Initial package

