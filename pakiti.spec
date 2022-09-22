## github commit ference 
%global commit ff9a35f2e82bf80b143553c06e7aabe3aff0ebf8
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global github_name pakiti

Summary:	Patching status monitoring tool
Name:		pakiti
Version:	3.0.2
Release:	11%{?dist}
URL:		https://github.com/CESNET/pakiti-client/
License:	ASL 2.0 and BSD
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires: make
BuildRequires:	perl-interpreter
BuildRequires:	perl-generators
BuildRequires:  /usr/bin/pod2man

BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%description
Runs rpm -qa or dpkg -l on the hosts and sends results to a central server.

Central server then process the results and checks whether the packages are
installed in the recent version. Central server also provides web GUI where
all results can be seen.

%package client
Summary:	Client for the Pakiti tool

%description client
Runs rpm -qa or dpkg -l, depends on the linux distro. Results are sent to the
central Pakiti server using openssl s_client or curl.

%prep
%setup -qn %{name}-%{version} 

%build
make

%install
install -D -m755 bin/pakiti-client   %{buildroot}%{_bindir}/pakiti-client
install -D -m644 pakiti-client.1 %{buildroot}%{_mandir}/man1/pakiti-client.1

%files client
%{_bindir}/*
%{_mandir}/man?/*

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 31 2017 Andrea Manzi <amanzi@cern.ch> - 3.0.2-1
- new upstream release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Feb 14 2016 Ralf Corsépius <corsepiu@fedoraproject.org> - 3.0.1-4
- Add BR: /usr/bin/pod2man (F24FTBFS, RHBZ#1307845).
- Add perl run-time deps to BRs.
- Add %%license.
- Modernize spec.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Adrien Devresse <adevress at cern.ch> - 3.0.1-1
 - Update to version 3.0.1 - bugzilla 1219337

* Tue Dec 09 2014 Adrien Devresse <adevress at cern.ch> - 3.0.0-1
 - Initial release for pakiti 3.0.0
