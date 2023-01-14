%global commit 6b89e56e24d76f96a89cfd147768e2a3e24eb48a
%global date 20230112
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           rpmdistro-repoquery
Version:        0^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        Tool to easily do repository queries for different distributions using DNF

License:        MIT
URL:            https://pagure.io/%{name}
Source:         %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildArch:      noarch

Requires:       distribution-gpg-keys
Requires:       dnf

%description
This tool utilizes DNF to let you query across several RPM-based Linux
distributions.

Currently, the tool supports the following distributions:

* Fedora
* Mageia
* openSUSE Leap
* openSUSE Tumbleweed
* CentOS (with EPEL)
* CentOS Stream (with EPEL and Hyperscale)
* Red Hat Enterprise Linux Universal Base Image (RHEL UBI)
* SUSE Linux Enterprise Base Container Image (SLE BCI)


%prep
%autosetup -p1 -n %{name}-%{shortcommit}


%build


%install
mkdir -p %{buildroot}%{_bindir}
install -p rpmdistro-{gendnfconf,repoquery} %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -pr distros %{buildroot}%{_datadir}/%{name}/


%files
%license LICENSE
%doc README.md
%{_bindir}/rpmdistro-gendnfconf
%{_bindir}/rpmdistro-repoquery
%{_datadir}/%{name}


%changelog
%autochangelog
