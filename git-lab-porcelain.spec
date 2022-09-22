%global fullcommit 51c3dc37cd68bc3fe44ef5ada61f5fff9b9b0042
%global shortcommit %(fcstr=%{fullcommit} && echo ${fcstr:0:8})
# %%global date        %%(date +%%Y%%m%%d) # hardcode so it matches a changelog
# month 33 is due to date format error in a previous rebuild
%global date        20203301
%global execname    git-lab

Name:      git-lab-porcelain
Version:   0
Release:   %{date}git%{shortcommit}%{?dist}.4
Summary:   Git porcelain for working with git-lab

License:   GPLv3
URL:       https://gitlab.com/nhorman/%{name}
Source0:   %{url}/-/archive/%{fullcommit}/%{name}-%{fullcommit}.tar.gz
BuildArch: noarch

Requires: python3-gitlab
Requires: python3-GitPython
Requires: python3-pycurl
Requires: python3-tabulate
Requires: curl

%description
A porcelain for git to facilitate command line creation/listing/editing
and reviewing of merge requests in git-lab.

%prep
%autosetup -n git-lab-porcelain-%{fullcommit}

%build
# nothing to do here

%install
mkdir -p %{buildroot}/%{_bindir}/
mkdir -p %{buildroot}/%{_mandir}/man1/
install -p -m 0755 %{execname} %{buildroot}/%{_bindir}/%{execname}
install -p -m 0644 man1/* %{buildroot}/%{_mandir}/man1/

%files
%{_bindir}/%{execname}
%{_mandir}/man1/*
%license LICENSE

%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-20203301git51c3dc37.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0-20203301git51c3dc37.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-20203301git51c3dc37.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0-20203301git51c3dc37.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 01 2020 Vladis Dronov <vdronoff+fedora@gmail.com> - 0-20203301git51c3dc37
- Update to latest upstream

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-2020325git75a12220.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Mar 25 2020 Neil Horman <nhorman@redhat.com>
- Update to latest upstream

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-20200123git4eeaa725.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 23 2020 Vladis Dronov <vdronoff+fedora@gmail.com> - 0-20200123git4eeaa725
- Update sources to the latest upstream

* Tue Jan 21 2020 Vladis Dronov <vdronoff+fedora@gmail.com> - 0-20200121git9f421f38
- Initial release for the Fedora 29-31 and Rawhide
