# The Clipper C++ crystallographic library already uses the name "clipper".
# The developer is fine with the choosen name.

Name:           polyclipping
Version:        6.4.2
Release:        %autorelease
%global so_version 22
Summary:        Polygon clipping library

# The entire source is BSL-1.0, except:
# - The contents of Documentation/Scripts/SyntaxHighlighter/ are “Dual licensed
#   under the MIT and GPL licenses“. These sources do not contribute to the
#   binary RPMs and are removed in %%prep.
License:        BSL-1.0
URL:            https://sourceforge.net/projects/polyclipping
Source0:        https://downloads.sourceforge.net/%{name}/clipper_ver%{version}.zip

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  dos2unix

%description
This library primarily performs the boolean clipping operations -
intersection, union, difference & xor - on 2D polygons. It also performs
polygon offsetting. The library handles complex (self-intersecting) polygons,
polygons with holes and polygons with overlapping co-linear edges.
Input polygons for clipping can use EvenOdd, NonZero, Positive and Negative
filling modes. The clipping code is based on the Vatti clipping algorithm,
and outperforms other clipping libraries.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -qc

# Delete binaries
find . \( -name "*.exe" -o -name "*.dll" \) -delete

# Delete bundled(js-syntaxhighlighter),
# https://github.com/syntaxhighlighter/syntaxhighlighter.
rm -rvf Documentation/Scripts/SyntaxHighlighter

# Correct line ends and encodings
find . -type f -exec dos2unix -k {} \;

for filename in "Third Party/perl/perl_readme.txt" README; do
  iconv -f iso8859-1 -t utf-8 "${filename}" > "${filename}".conv && \
    touch -r "${filename}" "${filename}".conv && \
    mv "${filename}".conv "${filename}"
done


%build
pushd cpp
  %cmake
  %cmake_build
popd


%install
pushd cpp
  %cmake_install

# Install agg header with corrected include statement
  sed -e 's/\.\.\/clipper\.hpp/clipper.hpp/' < cpp_agg/agg_conv_clipper.h > %{buildroot}/%{_includedir}/%{name}/agg_conv_clipper.h
popd


%files
%license License.txt
%doc README
%{_libdir}/lib%{name}.so.%{so_version}
%{_libdir}/lib%{name}.so.%{so_version}.*

%files devel
%doc "Third Party"
%{_datadir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}/
%{_libdir}/lib%{name}.so

%changelog
%autochangelog
