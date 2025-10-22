%global forgeurl https://salsa.debian.org/dns-team/dns-root-data

Name:           dns-root-data
Version:        2025080400
Release:        %autorelease
Summary:        DNS root hints and DNSSEC trust anchor

License:        MIT and CC0-1.0
# Part of data is covered by https://www.iana.org/help/licensing-terms
URL:            https://data.iana.org/root-anchors/
VCS:            git:%{forgeurl}.git
Source0:        %{forgeurl}/-/archive/debian/%{version}/dns-root-data-debian-%{version}.tar.bz2
Source1:        https://data.iana.org/root-anchors/icannbundle.pem
# This is DSA 1024b key. But no better signature is provided
Source2:        https://keyserver.ubuntu.com/pks/lookup?op=get&search=0xf0cb1a326bdf3f3efa3a01fa937bb869e3a238c5#/registry-admin.key

BuildRequires:  perl-interpreter
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(Net::DNS)
BuildRequires:  perl(DateTime::Format::RFC3339)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(Path::Tiny)
BuildRequires:  openssl
BuildRequires:  gnupg
BuildArch:      noarch

%description
This package contains various root zone related data as published
by IANA to be used by various DNS software as a common source
of DNS root zone data, namely:
 * Root Hints (root.hints)
 * Root Trust Anchors (root.key, root.ds)

%prep
%autosetup -n %{name}-debian-%{version}

%{gpgverify} --keyring=%{SOURCE2} --data=root.hints --signature=root.hints.sig
openssl smime -verify -CAfile %{SOURCE1} -inform DER -in root-anchors.p7s -content root-anchors.xml -out /dev/null


%build
./parse-root-anchors

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
install -p -m 0644 root.hints{,.sig} \
	%{buildroot}%{_datadir}/%{name}
install -p -m 0644 root-anchors.{p7s,xml} %{buildroot}%{_datadir}/%{name}
install -p -m 0644 root.{key,ds} %{buildroot}%{_datadir}/%{name}


%files
%license debian/copyright
%doc debian/README.Debian
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/root-anchors.xml
%{_datadir}/%{name}/root-anchors.p7s
%{_datadir}/%{name}/root.hints
%{_datadir}/%{name}/root.hints.sig
%{_datadir}/%{name}/root.key
%{_datadir}/%{name}/root.ds



%changelog
%autochangelog
