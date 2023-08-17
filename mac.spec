Name:           mac
Version:        10.18
Release:        %autorelease
Summary:        Monkey's Audio Codec

License:        BSD-3-Clause
URL:            https://monkeysaudio.com
Source:         %{url}/files/MAC_%(echo "%{version}" | tr -d .)_SDK.zip

BuildRequires:  cmake
BuildRequires:  gcc-c++

Requires:       %{name}-libs = %{version}-%{release}

%description
Monkey's Audio is a fast and easy way to compress digital music. Unlike
traditional methods such as mp3, ogg, or lqt that permanently discard
quality to save space, Monkey's Audio only makes perfect, bit-for-bit
copies of your music. That means it always sounds perfect – exactly the
same as the original. Even though the sound is perfect, it still saves a
lot of space.

%package        libs
Summary:        Library for Monkey's Audio Codec

%description    libs
The %{name}-libs package contains a library for Monkey's Audio Codec.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -c %{name}

# Drop prebuilt binaries and unused vendored dependencies
rm -r '3rd Party' Shared/{32,64} Source/'DirectShow Filter'

# Convert readme to UTF-8 and fix EOL encoding
iconv -f iso8859-1 -t utf-8 Readme.txt > Readme.txt.conv && \
  mv -f Readme.txt.conv Readme.txt
sed -i 's/\r$//' Readme.txt

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%{_bindir}/mac

%files libs
%license License.rtf
%doc Readme.txt
%{_libdir}/*.so.10*

%files devel
%{_includedir}/MAC/
%{_libdir}/*.so

%changelog
%autochangelog
