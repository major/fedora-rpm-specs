Name:           rtfilter
Version:        1.3
Release:        %autorelease
Summary:        Realtime digital filtering functions for multichannel signals

License:        LGPL-3.0-only
URL:            https://github.com/mmlabs-mindmaze/rtfilter
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  check-devel
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  python3

%description
rtfilter provides a library written in C implementing realtime digital
filtering functions for multichannel signals (i.e. filtering multiple
signals with the same filter). It implements FIR, IIR filters and
downsampler for float and double data type (both for real and complex
valued signal). Additional functions are also provided to design few
usual filters: Butterworth, Chebyshev, windowed sinc, analytical filter...

One of the main differences from other libraries providing digital signal
processing is that the filter functions have been specifically designed and
optimized for multichannel signals (from few channels to several hundred).
If data allows it, the library automatically switch to optimized SIMD
(Single Instruction Multiple Data) code, allowing to reduce by 3~4 the time
spent in processing the data.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{version}

%build
# docs produce HTML which bundles lots of js and css, so we don't build it
%meson -Ddocs=disabled
%meson_build

%install
%meson_install

# drop libtool
find %{buildroot} -name '*.la' -exec rm -f {} ';'
# drop installed copying in docdir
rm -f %{buildroot}%{_docdir}/%{name}/COPYING

%check
%meson_test

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/lib%{name}.so.1*

%files devel
%doc %{_docdir}/%{name}/examples
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/rtf*.h

%changelog
%autochangelog
