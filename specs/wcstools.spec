# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

%global build_type_safety_c 0

Name:       wcstools
Version:    3.9.7
Release:    %autorelease
Summary:    Software utilities to display and manipulate the WCS of a FITS image
License:    GPL-2.0-or-later
URL:        http://tdc-www.harvard.edu/wcstools
Source0:    http://tdc-www.harvard.edu/software/wcstools/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc

# Patch adjusted from Debian to create shared lib and rename it to avoid
# conflicts with Mark Calabretta's wcslib package.
Patch:      wcstools-3.9.7_rename-libwcs-to-libwcstools.patch

# Patch to rename some conflicting binaries
# new names in accordance to Debian renaming
# see also fedora#1450190
Patch:      wcstools-3.9.7_rename-binaries.patch

# Since there's no way to reach out upstream other than email
# and I don't get replies, this patch tries to fix build with GCC15
Patch:      fix_gcc15-c++23.patch

%description
Wcstools is a set of software utilities, written in C, which create,
display and manipulate the world coordinate system of a FITS or IRAF
image, using specific keywords in the image header which relate pixel
position within the image to position on the sky.  Auxiliary programs
search star catalogs and manipulate images.


%package libs
Summary:    Wcstools shared library
# most files have LGPL-2.0-or-later header
# COPYING is LGPL-2.1-only
License:    LGPL-2.0-or-later AND LGPL-2.1-only

%description libs
Shared library necessary to run wcstools and programs based on libwcs.


%package devel
Summary:    Libraries, includes, etc. used to develop an application with wcstools
License:    LGPL-2.0-or-later AND LGPL-2.1-only
Requires:   %{name}-libs%{_isa} = %{version}-%{release}
%description devel
This are the files needed to develop an application using wcstools.

%prep
%autosetup -p1

# Fix wrong FSF address in source headers
# asked upstream by mail to fix this
grep -rl '59 Temple Place, Suite 330, Boston, MA  02111-1307  USA' --include=*.{c,h} | xargs -i@ sed -i 's/59 Temple Place, Suite 330, Boston, MA  02111-1307  USA/51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA./g' @


%build
%make_build


%install
%{__mkdir_p} %{buildroot}%{_libdir}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__mkdir_p} %{buildroot}%{_includedir}/wcs
%{__mkdir_p} %{buildroot}%{_mandir}/man1
%{__install} -p bin/* %{buildroot}%{_bindir}
%{__cp} -a libwcs/*.so* %{buildroot}%{_libdir}
%{__install} -p -m 644 libwcs/*.h %{buildroot}%{_includedir}/wcs
%{__install} -p -m 644 man/man1/* %{buildroot}%{_mandir}/man1



%files
%license COPYING
%doc NEWS Readme Programs
%{_bindir}/*
%{_mandir}/man1/*

%files libs
%license libwcs/COPYING
%{_libdir}/*.so.1*

%files devel
%doc libwcs/NEWS
%{_libdir}/*.so
%{_includedir}/wcs


%changelog
%autochangelog
