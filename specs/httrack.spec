%global coucal_commit 73ada075553b7607d083037a87cb9c73b3683bfc
%global upstream_version 3.49.8-2

Name:           httrack
Version:        3.49.8^2
Release:        %autorelease
Summary:        Website copier and offline browser
License:        GPL-3.0-or-later AND BSD-3-Clause
URL:            https://github.com/xroche/httrack/
Source0:        https://github.com/xroche/httrack/archive/%{upstream_version}/%{name}-%{upstream_version}.tar.gz
Source1:        https://github.com/xroche/coucal/archive/%{coucal_commit}/coucal-%{coucal_commit}.tar.gz
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel
Requires:       hicolor-icon-theme
Requires:       xdg-utils
Provides:       bundled(coucal) = 0^git73ada07


%description
HTTrack is a free and easy-to-use offline browser utility. It allows the user 
to download a World Wide Web site from the Internet to a local directory, 
building recursively all directories, getting HTML, images, and other files 
from the server to your computer. HTTrack arranges the original site's 
relative link-structure. HTTrack can also update an existing mirrored site, 
and resume interrupted downloads. HTTrack is fully configurable, and has an 
integrated help system.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       openssl-devel%{?_isa}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -n %{name}-%{upstream_version} -p1 -a 1
rmdir src/coucal
mv coucal-%{coucal_commit} src/coucal
autoreconf -vfi

# Fix incorrect FSF address in libtest/readme.txt to satisfy rpmlint
sed -i '/write to the Free Software/{N;s|write to the Free Software\nFoundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.|see <https://www.gnu.org/licenses/>.|}' libtest/readme.txt

# Suppress rpmlint error.
iconv --from-code ISO8859-1 --to-code UTF-8 ./html/contact.html \
  --output contact.utf-8 && mv contact.utf-8 ./html/contact.html

# Fix AppStream icon validation error by removing the invalid stock icon tag
sed -i '/<icon type="stock">httrack<\/icon>/d' html/server/div/com.httrack.WebHTTrack.metainfo.xml

# Avoid duplicate files warning in rpmlint by symlinking license.txt to COPYING
rm -f license.txt
ln -s COPYING license.txt

%build
%configure  --disable-static \
            --disable-online-unit-tests \
            --htmldir=%{_pkgdocdir}/html \
            --docdir=%{_pkgdocdir}

# Remove rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%make_install

# Remove static libraries.
find %{buildroot} -type f -name "*.*a" -delete -print

# Remove unnecessary dynamic libraries from %%{_libdir}/httrack. These come
# from libtest, just a sample project from upstream.
rm -frv %{buildroot}%{_libdir}/%{name}

# Move libtest and templates from %%{_datadir}/httrack into %%{_pkgdocdir}.
mv %{buildroot}%{_datadir}/%{name}/libtest %{buildroot}%{_pkgdocdir}/libtest
mv %{buildroot}%{_datadir}/%{name}/templates %{buildroot}%{_pkgdocdir}/templates

# Now packaged in %%license
rm %{buildroot}%{_pkgdocdir}/html/license.txt

# Replace absolute symlink with a relative one to avoid rpmbuild warning
rm %{buildroot}%{_datadir}/%{name}/html
ln -s ../doc/%{name}/html %{buildroot}%{_datadir}/%{name}/html

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
make check -C tests

desktop-file-validate %{buildroot}%{_datadir}/applications/WebHTTrack.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/WebHTTrack-Websites.desktop
appstream-util validate-relax --nonet \
%{buildroot}%{_metainfodir}/com.httrack.WebHTTrack.metainfo.xml


%files
%{_pkgdocdir}
%exclude %{_pkgdocdir}/libtest
%license COPYING license.txt
%{_bindir}/htsserver
%{_bindir}/%{name}
%{_bindir}/proxytrack
%{_bindir}/webhttrack
%{_datadir}/applications/*WebHTTrack.desktop
%{_datadir}/applications/*WebHTTrack-Websites.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}*x*.xpm
%{_datadir}/%{name}/
%{_libdir}/libhtsjava.so.*
%{_libdir}/libhttrack.so.*
%{_mandir}/man1/htsserver.1*
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/proxytrack.1*
%{_mandir}/man1/webhttrack.1*
%{_metainfodir}/com.httrack.WebHTTrack.metainfo.xml

%files devel
%{_pkgdocdir}/libtest/
%{_includedir}/%{name}/
%{_libdir}/libhtsjava.so
%{_libdir}/libhttrack.so

%changelog
%autochangelog
