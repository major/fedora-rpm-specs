Name:           R-rjson
Version:        %R_rpm_version 0.2.23
Release:        %autorelease
Summary:        JSON for R

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel

%description
Converts R object into JSON objects and vice-versa.

%prep
%autosetup -c

chmod +x rjson/inst/rpc_server/server.r
chmod +x rjson/inst/rpc_server/start_server
# come on osx developer
sed -i 's|/usr/bin/r|/usr/bin/Rscript|g' rjson/inst/rpc_server/server.r

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
