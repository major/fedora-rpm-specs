%if 0%{?fedora} >= 43
ExcludeArch: %{ix86}
%endif

# About:
#   https://dev.mysql.com/doc/connectors/en/connector-odbc-installation-source-unix.html
Name:           mysql-connector-odbc
Version:        9.4.0
Release:        %autorelease
Summary:        ODBC driver for MySQL
# Automatically converted from old format: GPLv2 with exceptions - review is highly recommended.
License:        LicenseRef-Callaway-GPLv2-with-exceptions
URL:            https://dev.mysql.com/downloads/connector/odbc/

Source0:        http://dev.mysql.com/get/Downloads/Connector-ODBC/9.4/%{name}-%{version}-src.tar.gz
Patch0:         myodbc-64bit.patch
Patch3:         mysql-connector-odbc-rpath.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  mysql-devel >= 8
BuildRequires:  unixODBC-devel
BuildRequires:  libzstd-devel

# Required for GUI
#   GUI currently off. To switch it ON, uncomment gtk buildrequires and change CMake argument DISABLE_GUI
#   GUI does not make any sense on headless servers for example, which is a valid use case. I don't want
#   this tiny package to have dependency on X and GTK.
# BuildRequires:  gtk3-devel

%description
An ODBC (rev 3) driver for MySQL, for use with unixODBC.

%prep
%setup -q -n %{name}-%{version}-src
%patch -P0 -p1
%patch -P3 -p1

%build
%cmake \
        -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
        -DCMAKE_BUILD_TYPE=RelWithDebinfo \
        -DWITH_UNIXODBC=YES \
        -DRPM_BUILD=YES \
        -DMYSQLCLIENT_STATIC_LINKING=OFF \
        -DDISABLE_GUI=YES \
        -DBUILD_SHARED_LIBS=OFF

cmake -B %_vpath_builddir -LAH -N

%cmake_build

%install
%cmake_install

# Remove stuff not to be packaged, this tool is for archive distribution
# https://dev.mysql.com/doc/connector-odbc/en/connector-odbc-installation-binary-unix-tarball.html
rm %{buildroot}%{_bindir}/myodbc-installer

# Remove any file in /usr
find %{buildroot}/usr/ -maxdepth 1 -type f -delete

# Create a symlink for library to offer name that users are used to
ln -sf libmyodbc9w.so %{buildroot}%{_libdir}/libmyodbc9.so

# From Fedora 34, the unixODBC package introduced a libdir subdirectory for its plugins
mkdir %{buildroot}%{_libdir}/unixODBC
mv %{buildroot}%{_libdir}/libmyodbc*.so %{buildroot}%{_libdir}/unixODBC/

# Upstream provides a test suite with functional and regression tests.
# However, some tests fail, so it would deserve some more investigation.
# We don't include the test suite until it works fine.
rm -rf %{buildroot}/usr/test

%files
%license LICENSE.txt
%doc ChangeLog README.txt
%{_libdir}/unixODBC/lib*so

%changelog
%autochangelog
