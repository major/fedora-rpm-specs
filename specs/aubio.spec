# whether to do a verbose build
%bcond_without verbose_build
%if %{with verbose_build}
%global _verbose -v
%else
%global _verbose %{nil}
%endif

Name:           aubio
Version:        0.4.9
Release:        %autorelease
Summary:        An audio labeling tool

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://aubio.org/
Source0:        https://aubio.org/pub/aubio-%{version}.tar.bz2
Patch0:         %{name}-unversioned-python.patch
Patch1:         %{name}-python39.patch
Patch2:         %{name}-invalid-escape-sequence.patch
Patch3:         %{name}-imp-removed.patch
Patch4:         0001-py-add-const-qualifiers-to-ufuncs-prototypes-for-lat.patch

BuildRequires:  doxygen
BuildRequires:  fftw-devel
BuildRequires:  gcc
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel
BuildRequires:  python3-numpy
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  txt2man

Requires:       %{name}-python3 = %{version}-%{release}

%global _description %{expand:
aubio is a tool and library for audio labeling. Its features include
segmenting a sound file before each of its attacks, performing pitch
detection, tapping the beat and producing midi streams from live
audio. The name aubio comes from 'audio' with a typo: several
transcription errors are likely to be found in the results too.

The aim of this project is to provide these automatic labeling
features to other audio software. Functions can be used offline in
sound editors and software samplers, or online in audio effects and
virtual instruments.}

%description %_description

This package contains the aubio tool.

%package        lib
Summary:        An audio labeling library

%description    lib %_description

This package contains the aubio library.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-lib%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        python3
Summary:        Python 3 language bindings for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       python3

%description    python3
The %{name}-python3 package contains the Python 3 language bindings for
%{name}.

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%set_build_flags

%{python3} ./waf configure \
    --prefix="%_prefix" \
    --bindir="%_bindir" \
    --sysconfdir="%_sysconfdir" \
    --datadir="%_datadir" \
    --includedir="%_includedir" \
    --libdir="%_libdir" \
    --mandir="%_mandir" \
    --docdir="%_docdir" \
    --enable-fftw3f \
    --enable-complex \
    --enable-jack \
    --enable-samplerate

%{python3} ./waf build %{_verbose} %{?_smp_mflags}

%pyproject_wheel

%install
%{python3} ./waf --destdir=%{buildroot} %{_verbose} install
rm -f %{buildroot}%{_libdir}/*.a
rm -rf libaubio-doc
cp -r %{buildroot}%{_docdir}/libaubio-doc libaubio-doc
rm -rf %{buildroot}%{_docdir}/libaubio-doc

%pyproject_install
%pyproject_save_files %{name}

# Remove shebang from python files
sed -i -e '/^#![[:blank:]]*\//, 1d' %{buildroot}%{python3_sitearch}/%{name}/*.py

%check
export LD_LIBRARY_PATH="%{buildroot}%{_libdir}"
%pyproject_check_import

%files
%license COPYING
%doc AUTHORS ChangeLog README.md
%{_bindir}/*
%{_mandir}/man1/*

%files lib
%license COPYING
%{_libdir}/*.so.*

%files devel
%doc libaubio-doc/api
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so
%{_includedir}/aubio

%files python3 -f %{pyproject_files}

%changelog
%autochangelog
