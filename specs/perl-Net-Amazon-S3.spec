Name:       perl-Net-Amazon-S3
Version:    0.991
Release:    9%{?dist}
Summary:    Use the Amazon Simple Storage Service (S3)
# README.md reports the code is derived from an ADSL-licensed code.
License:    (GPL-1.0-or-later OR Artistic-1.0-Perl) AND ADSL
URL:        https://metacpan.org/release/Net-Amazon-S3
Source0:    https://cpan.metacpan.org/authors/id/B/BA/BARNEY/Net-Amazon-S3-%{version}.tar.gz
# Fix shebang
Patch0:     Net-Amazon-S3-0.86-Normalize-shellbang.patch
# Fix a content type check in multi-part upload, in upstream after 0.991,
# <https://github.com/rustyconover/net-amazon-s3/issues/124>
Patch1:     Net-Amazon-S3-0.991-Fix-initiate_multipart_upload-content-type-check.patch
BuildArch:  noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Stream::Bulk::Callback)
BuildRequires:  perl(DateTime::Format::HTTP)
BuildRequires:  perl(Digest::HMAC_SHA1)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Digest::MD5::File)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Exporter::Tiny)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::stat)
# Getopt::Long not used at tests
BuildRequires:  perl(Hash::Util)
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(HTTP::Status)
BuildRequires:  perl(IO::File) >= 1.14
# LWP 6.03 needed indirectly to support 100 Continue HTTP response
BuildRequires:  perl(LWP) >= 6.03
# HTTPS required because "secure" attribute is enabled by default
# LWP::Protocol::https not used at tests
BuildRequires:  perl(LWP::UserAgent::Determined)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(MIME::Types)
BuildRequires:  perl(Moose) >= 0.85
BuildRequires:  perl(Moose::Meta::Class)
BuildRequires:  perl(Moose::Object)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Role::Parameterized)
BuildRequires:  perl(MooseX::StrictConstructor) >= 0.16
BuildRequires:  perl(MooseX::Types::DateTime::MoreCoercions) >= 0.07
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(parent)
# Path::Class not used at tests
# Pod::Usage not used at tests
BuildRequires:  perl(Ref::Util)
BuildRequires:  perl(Regexp::Common)
BuildRequires:  perl(Safe::Isa)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(sort)
BuildRequires:  perl(Sub::Override)
# Term::Encoding is optional
# Term::ProgressBar::Simple not used at tests
BuildRequires:  perl(Test::Deep) >= 0.111
BuildRequires:  perl(Test::LWP::UserAgent)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(URI::QueryParam)
BuildRequires:  perl(VM::EC2::Security::CredentialCache)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(XML::LibXML::XPathContext)
# Tests:
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(lib)
BuildRequires:  perl(LWP::Simple)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::MockTime)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(utf8)
BuildRequires:  perl(vars)
# LWP 6.03 needed indirectly to support 100 Continue HTTP response
Requires:       perl(LWP) >= 6.03
# HTTPS required because "secure" attribute is enabled by default
Requires:       perl(LWP::Protocol::https)
Requires:       perl(VM::EC2::Security::CredentialCache)
# Provide modules loaded by a different file name, bug #1892877
Provides:       perl(Net::Amazon::S3::Operation::Object::Upload::Part) = %{version}
Provides:       perl(Net::Amazon::S3::Operation::Object::Upload::Parts) = %{version}
Provides:       perl(Net::Amazon::S3::Operation::Objects::Delete) = %{version}
Provides:       perl(Net::Amazon::S3::Operation::Objects::List) = %{version}

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::Deep\\)$

%description
This module provides a Perlish interface to Amazon S3. From the
developer blurb: "Amazon S3 is storage for the Internet. It is designed
to make web-scale computing easier for developers. Amazon S3 provides a
simple web services interface that can be used to store and retrieve any
amount of data, at any time, from anywhere on the web. It gives any
developer access to the same highly scalable, reliable, fast,
inexpensive data storage infrastructure that Amazon uses to run its own
global network of web sites. The service aims to maximize benefits of
scale and to pass those benefits on to developers".

To find out more about S3, please visit <http://s3.amazonaws.com/>.

%package -n perl-Shared-Examples-Net-Amazon-S3
Summary:    Example modules for Net::Amazon::S3 Perl tool kit
Requires:   perl-Net-Amazon-S3 = %{version}-%{release}
Requires:   perl(Test::Deep) >= 0.111

%description -n perl-Shared-Examples-Net-Amazon-S3
This package is an executable documentation for Net::Amazon::S3 Perl tool kit.

%package tests
Summary:        Tests for %{name}
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       perl-Test-Harness
Requires:       perl(Test::Deep) >= 0.111

%description tests
Tests from %{name}. Execute them
with "%{_libexecdir}/%{name}/test".

%prep
%autosetup -p1 -n Net-Amazon-S3-%{version}
# Get rid of unnecessary executable bits
find lib -name '*.pm' -exec chmod -c -x {} +
# Remove author tests
rm t/author-eol.t
perl -i -ne 'print $_ unless m{\A\Qt/author-eol.t\E}' MANIFEST
# Help generators to recognize a Perl code
for F in t/*.{t,pl}; do
    perl -i -MConfig -pe 'print qq{$Config{startperl}\n} if $. == 1 && !s{\A#!.*\bperl}{$Config{startperl}}' "$F"
    chmod +x "$F"
done

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}
# Install tests
mkdir -p %{buildroot}%{_libexecdir}/%{name}
cp -a t %{buildroot}%{_libexecdir}/%{name}
cat > %{buildroot}%{_libexecdir}/%{name}/test << 'EOF'
#!/bin/sh
unset AMAZON_S3_EXPENSIVE_TESTS AWS_ACCESS_KEY_ID
cd %{_libexecdir}/%{name} && exec prove -I . -j "$(getconf _NPROCESSORS_ONLN)"
EOF
chmod +x %{buildroot}%{_libexecdir}/%{name}/test

%check
unset AMAZON_S3_EXPENSIVE_TESTS AWS_ACCESS_KEY_ID
export HARNESS_OPTIONS=j$(perl -e 'if ($ARGV[0] =~ /.*-j([0-9][0-9]*).*/) {print $1} else {print 1}' -- '%{?_smp_mflags}')
make test

%files
%license LICENSE
# README.mkdn does not contain anything new
%doc CHANGES README README.md
%{_bindir}/s3cl
%dir %{perl_vendorlib}/Net
%dir %{perl_vendorlib}/Net/Amazon
%{perl_vendorlib}/Net/Amazon/S3
%{perl_vendorlib}/Net/Amazon/S3.pm
%{_mandir}/man1/s3cl.*
%{_mandir}/man3/Net::Amazon::S3.*
%{_mandir}/man3/Net::Amazon::S3::*

%files -n perl-Shared-Examples-Net-Amazon-S3
%dir %{perl_vendorlib}/Shared
%dir %{perl_vendorlib}/Shared/Examples
%dir %{perl_vendorlib}/Shared/Examples/Net
%dir %{perl_vendorlib}/Shared/Examples/Net/Amazon
%{perl_vendorlib}/Shared/Examples/Net/Amazon/S3
%{perl_vendorlib}/Shared/Examples/Net/Amazon/S3.pm
%{_mandir}/man3/Shared::Examples::Net::Amazon::S3.*
%{_mandir}/man3/Shared::Examples::Net::Amazon::S3::*

%files tests
%{_libexecdir}/%{name}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.991-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.991-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.991-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.991-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.991-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Mar 22 2023 Igor Raits <igot@gooddata.com> - 0.991-4
- Fix a content type check in multi-part upload (upstream bug #124)

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.991-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.991-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jul 18 2022 Petr Pisar <ppisar@redhat.com> - 0.991-1
- 0.991 bump

* Wed Jun 01 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.99-3
- Perl 5.36 rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.99-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 06 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.99-1
- 0.99 bump

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat May 22 2021 Jitka Plesnikova <jplesnik@redhat.com> - 0.98-2
- Perl 5.34 rebuild

* Wed Mar 24 2021 Petr Pisar <ppisar@redhat.com> - 0.98-1
- 0.98 bump
- Package tests

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.97-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Oct 30 2020 Petr Pisar <ppisar@redhat.com> - 0.97-2
- Provide modules loaded by a different file name (bug #1892877)

* Fri Oct 09 2020 Petr Pisar <ppisar@redhat.com> - 0.97-1
- 0.97 bump

* Thu Oct 08 2020 Petr Pisar <ppisar@redhat.com> - 0.96-1
- 0.96 bump

* Wed Oct 07 2020 Petr Pisar <ppisar@redhat.com> - 0.95-1
- 0.95 bump

* Tue Sep 29 2020 Petr Pisar <ppisar@redhat.com> - 0.94-1
- 0.94 bump

* Thu Aug 20 2020 Petr Pisar <ppisar@redhat.com> - 0.91-1
- 0.91 bump

* Wed Aug 19 2020 Petr Pisar <ppisar@redhat.com> - 0.90-1
- 0.90 bump

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.89-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jun 23 2020 Jitka Plesnikova <jplesnik@redhat.com> - 0.89-2
- Perl 5.32 rebuild

* Wed Feb 12 2020 Petr Pisar <ppisar@redhat.com> - 0.89-1
- 0.89 bump

* Mon Feb 03 2020 Petr Pisar <ppisar@redhat.com> - 0.88-1
- 0.88 bump

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.87-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 10 2019 Petr Pisar <ppisar@redhat.com> - 0.87-1
- 0.87 bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.86-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 0.86-2
- Perl 5.30 rebuild

* Mon Apr 15 2019 Petr Pisar <ppisar@redhat.com> - 0.86-1
- 0.86 bump

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.85-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 29 2018 Petr Pisar <ppisar@redhat.com> - 0.85-1
- 0.85 bump
- Example modules moved to separate perl-Shared-Examples-Net-Amazon-S3 package

* Tue Jul 17 2018 Petr Pisar <ppisar@redhat.com> - 0.84-1
- 0.84 bump

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.83-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 11 2018 Petr Pisar <ppisar@redhat.com> - 0.83-1
- 0.83 bump

* Mon Jul 09 2018 Petr Pisar <ppisar@redhat.com> - 0.82-1
- 0.82 bump

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 0.80-8
- Perl 5.28 rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 0.80-5
- Perl 5.26 rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 0.80-3
- Perl 5.24 rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.80-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Petr Pisar <ppisar@redhat.com> - 0.80-1
- 0.80 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.60-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 08 2015 Jitka Plesnikova <jplesnik@redhat.com> - 0.60-2
- Perl 5.22 rebuild

* Mon Dec 08 2014 Petr Pisar <ppisar@redhat.com> - 0.60-1
- 0.60 bump

* Tue Sep 02 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.59-4
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.59-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 27 2014 Petr Pisar <ppisar@redhat.com> - 0.59-2
- Enable s3cl tool (bug #995748)

* Sat Aug 10 2013 Paul Howarth <paul@city-fan.org> - 0.59-1
- Update to 0.59
- This release by PFIG -> update source URL
- Package upstream's LICENSE file
- Update dependencies as per upstream
- Exclude s3cl script for now as we can't satisfy its dependencies
- Drop %%defattr, redundant since rpm 4.4
- Use %%{_fixperms} macro rather than our own chmod incantation
- Allow for a future in which we might ship manpages compressed with something
  other than gzip

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.53-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.53-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.53-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 02 2012 Petr Pisar <ppisar@redhat.com> - 0.53-4
- Perl 5.16 rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.53-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 19 2011 Petr Sabata <contyk@redhat.com> - 0.53-2
- Perl mass rebuild

* Mon May 23 2011 Robert Rati <rrati@redhat> - 0.53-1
- Update to upstream 0.53

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.43-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 08 2010 Lubomir Rintel <lkundrak@v3.sk> - 0.43-7
- We install into vendorlib, need proper perl version require

* Tue May 04 2010 Marcela Maslanova <mmaslano@redhat.com> - 0.43-6
- Mass rebuild with perl-5.12.0

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.43-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.43-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Mar 24 2008  Robert Rati <rrati@redhat> - 0.43-3
- Fixed missing dependency on Class::Accessor perl module

* Thu Mar  6 2008  Robert Rati <rrati@redhat> - 0.43-2
- Package now owns all files/directories from Net on down
  to conform to packaging standards

* Thu Mar  6 2008  Robert Rati <rrati@redhat> - 0.43-1
- Initial release
