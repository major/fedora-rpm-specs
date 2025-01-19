# The value of Makefile LIBHTS_SOVERSION.
%global so_version 3

Name: htslib
Version: 1.15.1
Release: 8%{?dist}
Summary: C library for high-throughput sequencing data formats

# The entire source code is MIT/Expat except cram/ which is Modified-BSD.
# But as there is no "Expat" license in short name list, set "MIT".
# Expat license is same with MIT license.
# https://lists.fedoraproject.org/archives/list/legal@lists.fedoraproject.org/thread/C5AHVIW3F6LF5CYLR2PSHNANFYKP327P/
# Automatically converted from old format: MIT and BSD - review is highly recommended.
License: LicenseRef-Callaway-MIT AND LicenseRef-Callaway-BSD
URL: http://www.htslib.org
Source0: https://github.com/samtools/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2
# Work around a bug found using gcc-12 -O2.
# https://github.com/samtools/htscodecs/commit/65bb347f6b0ea7f4a00cb768b3d8004f24ae03c3
Patch0:  htslib-1.15.1-gcc12.patch

BuildRequires: gcc
BuildRequires: bzip2-devel
BuildRequires: libcurl-devel
BuildRequires: openssl-devel
BuildRequires: xz-devel
BuildRequires: zlib-devel
# It's used in make test.
BuildRequires: perl-interpreter
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(FindBin)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(lib)
BuildRequires: make

%description
HTSlib is an implementation of a unified C library for accessing common file
formats, such as SAM, CRAM and VCF, used for high-throughput sequencing data,
and is the core library used by samtools and bcftools.


%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package tools
Summary: Additional htslib-based tools
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
Includes the popular tabix indexer, which creates both .tbi and .csi formats,
the htsfile identifier tool, and the bgzip compression utility.


%prep
%setup -q
%patch -P0 -p1

%build
%configure CFLAGS="%{optflags}" LDFLAGS="%{build_ldflags}" \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --enable-plugins \
    --with-plugin-path='%{_usr}/local/libexec/htslib:$(plugindir)' \
    --enable-gcs \
    --enable-libcurl \
    --enable-s3
%make_build

# As we don't install libhts.a, the .private keywords are irrelevant.
sed -i -E '/^(Libs|Requires)\.private:/d' htslib.pc.tmp

%install
%make_install
pushd %{buildroot}/%{_libdir}
chmod 755 libhts.so.%{version}
popd

find %{buildroot} -name '*.la' -delete
rm -f %{buildroot}/%{_libdir}/libhts.a

%check
make test

%ldconfig_scriptlets

%files
%license LICENSE
%doc NEWS
%{_libdir}/libhts.so.%{version}
%{_libdir}/libhts.so.%{so_version}
# The plugin so files should be in the main package,
# as they are loaded when libhts.so.%%{so_version} is used.
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/hfile_gcs.so
%{_libexecdir}/%{name}/hfile_libcurl.so
%{_libexecdir}/%{name}/hfile_s3.so
%{_libexecdir}/%{name}/hfile_s3_write.so
# The man5 pages are aimed at users.
%{_mandir}/man5/faidx.5*
%{_mandir}/man5/sam.5*
%{_mandir}/man5/vcf.5*
%{_mandir}/man7/htslib-s3-plugin.7*

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/libhts.so
%{_libdir}/pkgconfig/htslib.pc

%files tools
%{_bindir}/bgzip
%{_bindir}/htsfile
%{_bindir}/tabix
%{_mandir}/man1/bgzip.1*
%{_mandir}/man1/htsfile.1*
%{_mandir}/man1/tabix.1*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 02 2024 Miroslav Suchý <msuchy@redhat.com> - 1.15.1-7
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.15.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Mon Aug 15 2022 John Marshall <jmarshall@hey.com> - 1.15.1-1
- Update to HTSlib version 1.15.1
- Backport htscodecs GCC 12 compatibility fix

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.13-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 14 2021 Sahana Prasad <sahana@redhat.com> - 1.13-2
- Rebuilt with OpenSSL 3.0.0

* Fri Jul 23 2021 John Marshall <jmarshall@hey.com> - 1.13-1
- Update to HTSlib version 1.13
- Bump soversion to 3 (the upstream soversion changed in HTSlib 1.10)
- Remove zlib-devel dependency as HTSlib headers no longer #include <zlib.h>
- Fix description: tabix creates .tbi/.csi by indexing other file formats
  (BAM, VCF, etc)
- Add new S3 man page and additional plugin

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Mar 17 2020 Jun Aruga <jaruga@redhat.com> - 1.9-6
- Fix the build failure adding perl(FindBin) and perl(lib) build dependencies.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 09 2019 Jun Aruga <jaruga@redhat.com> - 1.9-4
- Align the field delimiter as 1 space.
- Add check section and "make test" in it.

* Tue Nov 05 2019 John Marshall <jmarshall@users.sourceforge.net> - 1.9-4
- Remove unneeded pkg-config keywords for static linking, which generated
  unnecessary htslib-devel dependencies.
- Explicitly list zlib-devel dependency, needed for htslib-1.9.

* Sun Oct 27 2019 Jun Aruga <jaruga@redhat.com> - 1.9-3
- Fix a bug that %%{_libexecdir}/%%{name} directory is not removed,
  when uninstalling the package "rpm -e htslib".
- Add %%dir to directories to verify the files in the directory.

* Tue Oct 22 2019 Jun Aruga <jaruga@redhat.com> - 1.9-2
- Add configure script.
- Enable separately-compiled plugins.
- Enable support for Google Cloud Storage URLs.
- Enable libcurl-based support for http/https/etc URLs.
- Enable support for Amazon AWS S3 URLs.
- Move the man5 page files to main package.

* Fri Sep 06 2019 Jun Aruga <jaruga@redhat.com> - 1.9-1
- Update for htslib version 1.9

* Thu Jun 2 2016 Sam Nicholls <sam@samnicholls.net> - 1.3.1-4
- Fix changelog
- Add comment RE:bzip2/lzma support

* Sat May 28 2016 Sam Nicholls <sam@samnicholls.net> - 1.3.1-3
- Add LICENSE and NEWS to doc
- Remove unnecessary DESTDIR from call to make_install macro
- Remove explicit Provides

* Thu Apr 28 2016 Sam Nicholls <sam@samnicholls.net> - 1.3.1-1
- Alter permissions of SO to permit strip

* Tue Apr 26 2016 Sam Nicholls <sam@samnicholls.net> - 1.3.1-0
- Update for htslib version 1.3.1

* Tue Apr 12 2016 Sam Nicholls <sam@samnicholls.net> - 1.3.0-0
- Initial version
