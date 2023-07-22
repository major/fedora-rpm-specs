Name: mod_ruid2
Version: 0.9.8
Release: 20%{?dist}
Summary: A suexec module for Apache

License: ASL 2.0
URL: http://sourceforge.net/projects/mod-ruid/
Source0: http://downloads.sourceforge.net/project/mod-ruid/mod_ruid2/mod_ruid2-%{version}.tar.bz2
Source1: mod_ruid2.conf
Source2: 10-mod_ruid2.conf

BuildRequires:  gcc
BuildRequires: httpd-devel libcap-devel

Requires: httpd
Requires: httpd-mmn = %{_httpd_mmn}

%description
mod_ruid2 is a suexec module for Apache which takes advantage of 
POSIX.1e capabilities to increase performance.

%prep
%setup -q


%build
apxs -l cap -c %{name}.c


%install
mkdir -p %{buildroot}%{_httpd_confdir}
mkdir -p %{buildroot}%{_libdir}/httpd/modules
install -m 700 -d %{buildroot}%{_localstatedir}/lib/%{name}

%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
# 2.4-style
install -Dp -m0644 %{SOURCE2} %{buildroot}%{_httpd_modconfdir}/10-mod_ruid2.conf
install -Dp -m0644 %{SOURCE1} %{buildroot}%{_httpd_confdir}/mod_ruid2.conf
%else
# 2.2-style
install -d -m0755 %{buildroot}%{_httpd_confdir}
cat %{SOURCE2} %{SOURCE1} > %{buildroot}%{_httpd_confdir}/mod_ruid2.conf
%endif
install -m 755 .libs/mod_ruid2.so %{buildroot}%{_httpd_moddir}


%files
%doc README
%{_httpd_moddir}/mod_ruid2.so
%config(noreplace) %{_httpd_confdir}/*.conf

%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
    %config(noreplace) %{_httpd_modconfdir}/*.conf
%endif

%{!?_licensedir:%global license %%doc}
%license LICENSE

%changelog
* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 29 2018 Athmane Madjoudj <athmane@fedoraproject.org> - 0.9.8-9
- Remove the custom macros since they are defined in httpd-devel

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Mar 16 2015 Athmane Madjoudj <athmane@fedoraproject.org> 0.9.8-2
- Fix license issue
- Add a workarround for epel 

* Sun Apr 20 2014 Athmane Madjoudj <athmane@fedoraproject.org> 0.9.8-1
- Initial spec.

