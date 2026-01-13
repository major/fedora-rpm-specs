Name:           cliquer
Version:        1.23
Release:        %autorelease
Summary:        Find cliques in arbitrary weighted graphs

License:        GPL-2.0-or-later
URL:            https://users.aalto.fi/~pat/cliquer.html
Source0:        https://github.com/dimpase/autocliquer/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        http://users.aalto.fi/~pat/%{name}/%{name}_fm.pdf
Source2:        http://users.aalto.fi/~pat/%{name}/%{name}.pdf
Source3:        http://users.aalto.fi/~pat/%{name}/%{name}_bm.pdf
# Man page formatting by Jerry James, text from the sources
Source4:        %{name}.1

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

BuildRequires:  gcc
BuildRequires:  make

%description
The main cliquer package contains a command-line interface to the cliquer
library.  Note that the upstream binary name is "cl", which is too generic for
Fedora.  Therefore, the binary is named "cliquer".

%package libs
Summary:        Library to find cliques in arbitrary weighted graphs

%description libs
Cliquer is a set of C routines for finding cliques in an arbitrary weighted
graph.  It uses an exact branch-and-bound algorithm developed by Patric
Östergård.  It is designed with the aim of being efficient while still being
flexible and easy to use.

%package devel
Summary:        Development files for cliquer
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Development files for cliquer.

%prep
%autosetup -p1
cp -p %{SOURCE1} %{SOURCE2} %{SOURCE3} .

%conf
sed -i \
    's/59 Temple Place, Suite 330, Boston, MA  02111-1307/51 Franklin Street, Suite 500, Boston, MA  02110-1335/' \
    COPYING

%build
%configure --disable-static --disable-silent-rules

# Get rid of undesirable hardcoded rpaths; workaround libtool reordering
# -Wl,--as-needed after all the libraries.
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool

%make_build

%install
%make_install

# Add missing executable bit
chmod 0755 %{buildroot}%{_libdir}/libcliquer.so.1.*

# We do not want to install the examples
rm -fr %{buildroot}%{_datadir}/%{name}

# The name "cl" is very short and ambiguous
mv %{buildroot}%{_bindir}/cl %{buildroot}%{_bindir}/%{name}

# Install the man page
mkdir -p %{buildroot}%{_mandir}/man1
cp -p %{SOURCE4} %{buildroot}%{_mandir}/man1

%check
LD_LIBRARY_PATH=$PWD make test

%files
%doc cliquer*.pdf
%{_bindir}/%{name}
%{_mandir}/man1/*

%files libs
%doc ChangeLog README
%license COPYING
%{_libdir}/libcliquer.so.1{,.*}

%files devel
%{_includedir}/%{name}/
%{_libdir}/libcliquer.so
%{_libdir}/pkgconfig/libcliquer.pc

%changelog
%autochangelog
