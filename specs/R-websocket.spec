Name:           R-websocket
Version:        %R_rpm_version 1.4.4
Release:        %autorelease
Summary:        'WebSocket' Client Library

License:        GPL-2.0-only
URL:            %{cran_url}
Source:         %{cran_source}

BuildRequires:  R-devel
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(websocketpp)

%description
Provides a WebSocket client interface for R. WebSocket is a protocol for
low-overhead real-time communication:
<https://en.wikipedia.org/wiki/WebSocket>.

%prep
%autosetup -c
# unbundle https://github.com/rstudio/websocket/issues/59
pushd websocket/src/lib
    rm -rf websocketpp update.sh
    cp -r %{_includedir}/websocketpp .
    find . -type f -print0 | xargs -0 sed -i 's/websocketpp::/ws_websocketpp::/g'
    find . -type f -print0 | xargs -0 sed -i 's/namespace websocketpp/namespace ws_websocketpp/g'
    find . -type f -print0 | xargs -0 sed -i 's/&std::cout/(std::ostream*)\&WrappedOstream::cout/g'
    find . -type f -print0 | xargs -0 sed -i 's/&std::cerr/(std::ostream*)\&WrappedOstream::cerr/g'
popd
# remove https://github.com/rstudio/websocket/issues/111
sed -i '/openssl\/engine/d' websocket/src/tests/main.c

%generate_buildrequires
%R_buildrequires

%build

%install
%R_install
%R_save_files

%check
%R_check \--no-tests

%files -f %{R_files}

%changelog
%autochangelog
