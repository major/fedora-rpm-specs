%global baseversion 1.0.0
%global prerel rc
%global upstream_tag %{baseversion}%{?prerel}

Name:           nginx-mod-brotli
Version:        %{baseversion}%{?prerel:~%{prerel}}
Release:        %autorelease
Summary:        NGINX module for Brotli compression

License:        BSD-2-Clause
URL:            https://github.com/google/ngx_brotli
Source:         %{url}/archive/v%{upstream_tag}/ngx_brotli-%{upstream_tag}.tar.gz
# Patches to ensure system's brotli library is used
Patch:          https://patch-diff.githubusercontent.com/raw/google/ngx_brotli/pull/150.patch
Patch:          https://patch-diff.githubusercontent.com/raw/google/ngx_brotli/pull/172.patch

BuildRequires:  gcc
BuildRequires:  nginx-mod-devel
BuildRequires:  pkgconfig(libbrotlienc)


%description
%{summary}.

%prep
%autosetup -n ngx_brotli-%{upstream_tag} -p1


%build
%nginx_modconfigure
%nginx_modbuild


%install
pushd %{_vpath_builddir}
install -dm 0755 %{buildroot}%{nginx_moddir}
install -pm 0755 ngx_http_brotli_filter_module.so %{buildroot}%{nginx_moddir}
install -pm 0755 ngx_http_brotli_static_module.so %{buildroot}%{nginx_moddir}
install -dm 0755 %{buildroot}%{nginx_modconfdir}
cat <<EOF > %{buildroot}%{nginx_modconfdir}/mod-brotli.conf
load_module "%{nginx_moddir}/ngx_http_brotli_filter_module.so";
load_module "%{nginx_moddir}/ngx_http_brotli_static_module.so";
EOF
popd


%files
%license LICENSE
%doc README.md
%{nginx_moddir}/ngx_http_brotli_filter_module.so
%{nginx_moddir}/ngx_http_brotli_static_module.so
%{nginx_modconfdir}/mod-brotli.conf


%changelog
%autochangelog
