Name:		rakudo-MIME-Base64
Version:	1.2.1
Release:	12%{?dist}
Summary:	A Perl6 implementation of MIME::Base64 for ASCII strings

License:	Artistic 2.0
URL:		https://github.com/perl6/Perl6-MIME-Base64

# The source is provided from the URL
#   https://github.com/perl6/Perl6-MIME-Base64/archive/v1.2.1.tar.gz
# but the filename at the end of the URL do not match the filename that will
# be downloaded. The file that will be downloaded is:
#   Perl6-MIME-Base64-1.2.1.tar.gz
# For this reason a copy of the orginal source file is provided
# from the FTP-Server.  
Source0:	ftp://ftp.uni-siegen.de/pub/Perl6Mod.src/Perl6-MIME-Base64-%{version}.tar.gz

BuildRequires:	rakudo >= %rakudo_rpm_version
Requires:	rakudo >= %rakudo_rpm_version


%description
MIME::Base64 - Encoding and decoding Base64 ASCII strings. A Perl6
implementation of MIME::Base64 to encoding and decoding to and from base64.


%prep
%setup -q -n Perl6-MIME-Base64-%{version}


%install
export QA_SKIP_BUILD_ROOT=1
%perl6_mod_inst --to=%{buildroot}%{perl6_vendor_dir} --for=vendor


%check
perl6 -Ilib t/*.t


%files
%doc README.md
%license LICENSE
%{perl6_vendor_dir}/*/*


%changelog
* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jul 28 2019 Gerd Pokorra <gp@zimt.uni-siegen.de> 1.2.1-6
- add QA_SKIP_BUILD_ROOT=1
- remove of excluding the architectures s390x and ppc64

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Sep 21 2017 Gerd Pokorra <gp@zimt.uni-siegen.de> 1.2.1-1
- create initial spec file
