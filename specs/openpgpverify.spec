Name:           openpgpverify
Version:        2.2
Release:        %autorelease
Summary:        Signature verifier for easy and safe scripting

License:        Boehm-GC
URL:            https://src.fedoraproject.org/rpms/openpgpverify
Source:         openpgpverify
Source:         macros.openpgpverify.in
Source:         license.txt
BuildArch:      noarch

Requires:       grep sequoia-sqv

%description
OpenPGPverify is a wrapper around Sequoia's sqv. It verifies a file against an
OpenPGP signature and one or more keyrings. Rather than assuming manual use by
a knowledgeable user, OpenPGPverify is designed to be easy to use safely in a
script.

%prep
# Enable use of filenames instead of source numbers.
%setup -c -T
cp --preserve=timestamps %{sources} .

%conf
# Convey the location of the shellscript to macros.openpgpverify. To keep build
# dependencies minimal, do substitution in Bash instead of something like Sed.
macrofile=$(<macros.openpgpverify.in)
echo -E "${macrofile/@libexecdir@/'%{_libexecdir}'}" >macros.openpgpverify

%install
mkdir --parents %{buildroot}%{rpmmacrodir} %{buildroot}%{_libexecdir}
cp --preserve=timestamps openpgpverify %{buildroot}%{_libexecdir}/
cp macros.openpgpverify %{buildroot}%{rpmmacrodir}/

%files
%attr(0755,-,-) %{_libexecdir}/openpgpverify
%attr(0644,-,-) %{rpmmacrodir}/macros.openpgpverify
%license license.txt

%changelog
%autochangelog
