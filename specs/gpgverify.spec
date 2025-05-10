Name:           gpgverify
Version:        2.1
Release:        2%{?dist}
Summary:        Signature verifier for easy and safe scripting

License:        Boehm-GC
URL:            https://src.fedoraproject.org/rpms/gpgverify
Source:         gpgverify
Source:         macros.gpgverify
Source:         license.txt
BuildArch:      noarch

Requires:       grep gnupg2

%description
GPGverify is a wrapper around GnuPG's gpgv. It verifies a file against an
OpenPGP signature and one or more keyrings. Rather than assuming manual use by
a knowledgeable user, GPGverify is designed to be easy to use safely in a
script. It avoids various unsafe ways of using gpgv that could make a script
vulnerable.

%prep
# Enable use of filenames instead of source numbers.
%setup -c -T
cp --preserve=timestamps %{sources} .

%install
mkdir --parents %{buildroot}%{rpmmacrodir} %{buildroot}%{_libexecdir}
cp --preserve=timestamps gpgverify %{buildroot}%{_libexecdir}/
cp --preserve=timestamps macros.gpgverify %{buildroot}%{rpmmacrodir}/

%files
%attr(0755,-,-) %{_libexecdir}/gpgverify
%attr(0644,-,-) %{rpmmacrodir}/macros.gpgverify
%license license.txt

%changelog
* Wed May 07 2025 Björn Persson <Bjorn@Rombobjörn.se> - 2.1-2
- Added a separate license file.

* Mon Apr 14 2025 Björn Persson <Bjorn@Rombobjörn.se> - 2.1-1
- GPGverify has been split out from redhat-rpm-config.
