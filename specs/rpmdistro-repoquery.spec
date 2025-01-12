%global commit 2dd813432d5c832704077c4555f3d0e459e438c9
%global date 20250110
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           rpmdistro-repoquery
Version:        0^%{date}git%{shortcommit}
Release:        %autorelease
Summary:        Tool to easily do repository queries for different distributions using DNF

License:        MIT
URL:            https://pagure.io/%{name}
Source:         %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       distribution-gpg-keys
%if 0%{?fedora} >= 41 || 0%{?rhel} >= 11
Requires:       dnf5
%else
Requires:       dnf
%endif

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
install -p rpmdistro-repoquery %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -pr distros %{buildroot}%{_datadir}/%{name}/


%files
%license LICENSE
%doc README.md
%{_bindir}/rpmdistro-repoquery
%{_datadir}/%{name}


%changelog
%autochangelog
