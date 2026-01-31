# RPM Spec file for redwax-tool

Name:          redwax-tool
Version:       1.0.0
Release:       %autorelease -b 1
ExcludeArch:   %{ix86}
Summary:       The redwax tool
License:       Apache-2.0
Source0:       https://archive.redwax.eu/dist/rt/%{name}-%{version}/%{name}-%{version}.tar.bz2
Source1:       https://archive.redwax.eu/dist/rt/%{name}-%{version}/%{name}-%{version}.tar.bz2.asc
Source2:       https://source.redwax.eu/svn/dist/rt/keys/KEYS
Source3:       redwax-test-certificates.pem
Url:           https://redwax.eu/rs/
BuildRequires: gnupg2
BuildRequires: gcc
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig(apr-1)
BuildRequires: pkgconfig(apr-util-1)
BuildRequires: pkgconfig(libcrypto)
BuildRequires: pkgconfig(nss)
BuildRequires: pkgconfig(p11-kit-1)
BuildRequires: pkgconfig(libical)
BuildRequires: pkgconfig(ldns)
BuildRequires: pkgconfig(libunbound)

%description
The redwax tool allows certificates and keys in a range of formats to
be read, searched for, and converted into other formats as needed by
common services.

%prep
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q
%build
%configure --with-openssl --with-nss --with-p11-kit --with-libical --with-ldns --with-unbound --with-bash-completion-dir=%{bash_completions_dir}
%make_build

%install
%make_install

%check
./redwax-tool --pem-in '%{SOURCE3}' --filter-expiry=ignore --filter verify --metadata-out -

%files
%{_bindir}/redwax-tool
%{_mandir}/man1/redwax-tool.1*
%{bash_completions_dir}/redwax-tool

%doc AUTHORS ChangeLog README
%license COPYING

%changelog
* Thu Jan 29 2026 Graham Leggett <minfrin@sharp.fm> 1.0.0-4
- Fix test case in spec file
* Mon Jun 23 2025 Graham Leggett <minfrin@sharp.fm> 1.0.0-1
- Major release
* Thu Feb 27 2025 Graham Leggett <minfrin@sharp.fm> 0.9.9-1
- Bugfix release
* Thu Feb 27 2025 Graham Leggett <minfrin@sharp.fm> 0.9.8-1
- Bugfix release
* Thu Nov 28 2024 Graham Leggett <minfrin@sharp.fm> 0.9.7-1
- Bugfix release
* Mon Nov 11 2024 Graham Leggett <minfrin@sharp.fm> 0.9.6-1
- Feature release
* Mon Nov 11 2024 Graham Leggett <minfrin@sharp.fm> 0.9.5-1
- Feature release
* Thu Feb 08 2024 Graham Leggett <minfrin@sharp.fm> 0.9.4-1
- Feature release
* Sun Oct 15 2023 Graham Leggett <minfrin@sharp.fm> 0.9.3-1
- Feature release
* Mon Jan 02 2023 Graham Leggett <minfrin@sharp.fm> 0.9.2-1
- Feature release
* Sat Dec 11 2021 Graham Leggett <minfrin@sharp.fm> 0.9.1-1
- Feature release
* Sat May 15 2021 Graham Leggett <minfrin@sharp.fm> 0.9.0-1
- Initial release
