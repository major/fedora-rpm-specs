%global io_compress_version 2.201

Name:           perl-Archive-Zip-SimpleZip
Version:        1.000
Release:        2%{?dist}
Summary:        Create Zip Archives
License:        GPL+ or Artistic
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
