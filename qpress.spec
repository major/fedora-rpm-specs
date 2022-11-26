%global forgeurl https://github.com/PierreLvx/qpress

Name:           qpress
Version:        20220819
Release:        %autorelease
Summary:        A portable file archiver using QuickLZ

License:        GPL-1.0-only and GPL-2.0-only and GPL-3.0-only
URL:            https://www.quicklz.com
Source0:        %{forgeurl}/archive/%{version}/%{name}-%{version}.tar.gz
# Rework makefile to ease packaging
Patch1:         https://github.com/PierreLvx/qpress/pull/8.patch
# Add license texts
Patch2:         https://github.com/PierreLvx/qpress/pull/9.patch

BuildRequires:  gcc-c++
BuildRequires:  make

Provides:       bundled(quicklz) = 1.4.1

%description
qpress is a portable file archiver using QuickLZ and designed to utilize fast
storage systems to their max. It's often faster than file copy because the
destination is smaller than the source.

%prep
%autosetup -p1

%build
%set_build_flags
# https://gcc.gnu.org/bugzilla/show_bug.cgi?id=85783
export CXXFLAGS="$CXXFLAGS -Wno-alloc-size-larger-than"
%make_build

%install
%make_install PREFIX="%{_prefix}"

%files
%license LICENSE.GPL-1.0 LICENSE.GPL-2.0 LICENSE.GPL-3.0
%doc readme.md
%{_bindir}/%{name}

%changelog
%autochangelog
