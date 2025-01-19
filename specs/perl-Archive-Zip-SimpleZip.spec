%global io_compress_version 2.213

Name:           perl-Archive-Zip-SimpleZip
Version:        1.002
Release:        2%{?dist}
Summary:        Create Zip Archives
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Archive-Zip-SimpleZip/
Source0:        https://cpan.metacpan.org/modules/by-module/Archive/Archive-Zip-SimpleZip-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(bytes)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Compress::Raw::Zlib)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Devel::Peek)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76 
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Compress::Adapter::Deflate) >= %{io_compress_version}
BuildRequires:  perl(IO::Compress::Base) >= %{io_compress_version}
BuildRequires:  perl(IO::Compress::Base::Common) >= %{io_compress_version}
BuildRequires:  perl(IO::Compress::Bzip2) >= %{io_compress_version}
BuildRequires:  perl(IO::Compress::Lzma) >= %{io_compress_version}
BuildRequires:  perl(IO::Compress::RawDeflate) >= %{io_compress_version}
BuildRequires:  perl(IO::Compress::Xz) >= %{io_compress_version}
BuildRequires:  perl(IO::Compress::Zip) >= %{io_compress_version}
BuildRequires:  perl(IO::Compress::Zip::Constants) >= %{io_compress_version}
BuildRequires:  perl(IO::Compress::Zstd) >= %{io_compress_version}
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Uncompress::Base) >= %{io_compress_version}
BuildRequires:  perl(IO::Uncompress::Bunzip2) >= %{io_compress_version}
BuildRequires:  perl(IO::Uncompress::RawInflate) >= %{io_compress_version}
BuildRequires:  perl(IO::Uncompress::UnLzma) >= %{io_compress_version}
BuildRequires:  perl(IO::Uncompress::UnXz) >= %{io_compress_version}
BuildRequires:  perl(IO::Uncompress::Unzip) >= %{io_compress_version}
BuildRequires:  perl(IO::Uncompress::UnZstd) >= %{io_compress_version}
BuildRequires:  perl(Perl::OSType)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::CPAN::Meta::JSON)
BuildRequires:  perl(Test::CPAN::Meta)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(Test::Pod) >=  1.00
Requires:       perl(IO::Compress::Base) >= %{io_compress_version}
Requires:       perl(IO::Compress::Bzip2) >= %{io_compress_version}
Requires:       perl(IO::Compress::Lzma) >= %{io_compress_version}
Requires:       perl(IO::Compress::RawDeflate) >= %{io_compress_version}
Requires:       perl(IO::Compress::Xz) >= %{io_compress_version}
Requires:       perl(IO::Compress::Zstd) >= %{io_compress_version}
Requires:       perl(IO::Uncompress::Base) >= %{io_compress_version}
Requires:       perl(IO::Uncompress::Bunzip2) >= %{io_compress_version}
Requires:       perl(IO::Uncompress::RawInflate) >= %{io_compress_version}
Requires:       perl(IO::Uncompress::UnLzma) >= %{io_compress_version}
Requires:       perl(IO::Uncompress::UnXz) >= %{io_compress_version}
Requires:       perl(IO::Uncompress::UnZstd) >= %{io_compress_version}

%description
Archive::Zip::SimpleZip is a module that allows the creation of Zip
archives. For reading Zip archives, there is a companion module, called
Archive::Zip::SimpleUnzip, that can read Zip archives.


%prep
%setup -q -n Archive-Zip-SimpleZip-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build


%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.002-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 09 2024 Xavier Bachelot <xavier@bachelot.org> - 1.002-1
- Update to 1.002 (RHBZ#2309002)

* Mon Aug 05 2024 Miroslav Suchý <msuchy@redhat.com> - 1.000-8
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.000-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jun 30 2022 Jitka Plesnikova <jplesnik@redhat.com> - 1.000-1
- 1.000 bump

* Tue May 31 2022 Jitka Plesnikova <jplesnik@redhat.com> - 0.040-4
- Perl 5.36 rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.040-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Nov 18 2021 Xavier Bachelot <xavier@bachelot.org> 0.040-2
- Review fixes

* Thu Oct 07 2021 Xavier Bachelot <xavier@bachelot.org> 0.040-1
- Initial package
