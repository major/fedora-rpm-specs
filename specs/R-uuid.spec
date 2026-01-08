Name:           R-uuid
Version:        %R_rpm_version 1.2-1
Release:        %autorelease
Summary:        Tools for generating and handling of UUIDs

License:        MIT
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
BuildRequires:  libuuid-devel

%description
Tools for generating and handling of UUIDs (Universally Unique
Identifiers).

%prep
%autosetup -c
# Use system libuuid.
pushd uuid
rm configure.ac configure src/Makevars.in src/[a-z]*.[ch]
sed -i -e '/configure/d' -e '/Makevars/d' -e '/src\/[a-z].*.[ch]/d' MD5
rm -r src/config.h.in src/win32
sed -i -e '/config.h/d' MD5
cat > src/Makevars << EOF
PKG_CFLAGS = \$(shell pkg-config --cflags uuid)
PKG_LIBS = \$(shell pkg-config --libs uuid)
EOF
popd

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check

%files -f %{R_files}

%changelog
%autochangelog
