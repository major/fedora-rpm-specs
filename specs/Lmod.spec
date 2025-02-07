%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)
# We'd like to be noarch, but Lmod encodes the system lua path
%global debug_package %{nil}

Name:           Lmod
Version:        8.7.56
Release:        %autorelease
Summary:        Environmental Modules System in Lua

# Lmod-5.3.2/tools/base64.lua is LGPLv2
License:        MIT AND LGPL-2.0-only
URL:            https://tacc.utexas.edu/research/tacc-research/lmod/
Source0:        https://github.com/TACC/Lmod/archive/%{version}/Lmod-%{version}.tar.gz
Source1:        macros.%{name}

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  bc
BuildRequires:  lua-devel
BuildRequires:  lua-filesystem
BuildRequires:  lua-json
BuildRequires:  lua-posix
BuildRequires:  lua-term
BuildRequires:  tcl-devel
BuildRequires:  zsh
Requires:       lua-filesystem
Requires:       lua-json
Requires:       lua-posix
Requires:       lua-term
%if 0%{?rhel} && 0%{?rhel} <= 6
Requires:       /bin/ps
%else
Requires:       /usr/bin/ps
%endif
%if 0%{?fedora} || 0%{?rhel} >= 8
Requires(post): coreutils
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives
%endif
Provides:       environment(modules)

%description
Lmod is a Lua based module system that easily handles the MODULEPATH
Hierarchical problem.  Environment Modules provide a convenient way to
dynamically change the users' environment through modulefiles. This includes
easily adding or removing directories to the PATH environment variable.
Modulefiles for library packages provide environment variables that specify
where the library and header files can be found.


%prep
%autosetup -p1
sed -i -e 's,/usr/bin/env ,/usr/bin/,' src/*.tcl
# Remove bundled lua-filesystem and lua-term
rm -r pkgs/{luafilesystem,term} tools/json.lua
#sed -i -e 's, pkgs , ,' Makefile.in
# Remove unneeded shbangs
sed -i -e '/^#!/d' init/*.in


%build
%if 0%{?rhel} && 0%{?rhel} <= 6
%configure --prefix=%{_datadir} PS=/bin/ps
%else
%configure --prefix=%{_datadir} PS=/usr/bin/ps
%endif
%make_build


%install
# tcl2lua is built here
%set_build_flags
%make_install
# init scripts are sourced
find %{buildroot}%{_datadir}/lmod/%{version}/init -type f -exec chmod -x {} +
mkdir -p %{buildroot}%{_sysconfdir}/modulefiles
mkdir -p %{buildroot}%{_datadir}/modulefiles
mkdir -p %{buildroot}%{_sysconfdir}/profile.d %{buildroot}%{_datadir}/fish/vendor_conf.d
%if 0%{?fedora} || 0%{?rhel} >= 8
# Setup for alternatives on Fedora
touch %{buildroot}%{_sysconfdir}/profile.d/modules.{csh,sh} \
      %{buildroot}%{_datadir}/fish/vendor_conf.d/modules.fish
%endif

# Fedora defaults
cat <<'EOF' > %{buildroot}%{_sysconfdir}/profile.d/00-modulepath.sh
[ -z "$MODULEPATH" ] &&
  [ "$(readlink /etc/alternatives/modules.sh)" = "/usr/share/lmod/lmod/init/profile" -o -f /etc/profile.d/z00_lmod.sh ] &&
  export MODULEPATH=%{_sysconfdir}/modulefiles:%{_datadir}/modulefiles || :
EOF

cat << 'EOF' > %{buildroot}%{_sysconfdir}/profile.d/00-modulepath.csh
if (! $?MODULEPATH && ( `readlink /etc/alternatives/modules.csh` == /usr/share/lmod/lmod/init/cshrc || -f /etc/profile.d/z00_lmod.csh ) ) then
  setenv MODULEPATH %{_sysconfdir}/modulefiles:%{_datadir}/modulefiles
endif
EOF

# Add a snippet to make sure that the 00-modulepath.* is included, when
# the user calls /etc/profile.d/modules.sh directly, just below
# the shbang line.
sed -i '2i\. /etc/profile.d/00-modulepath.sh\n' \
  %{buildroot}%{_datadir}/lmod/lmod/init/profile

%if 0%{?rhel} && 0%{?rhel} < 8
# Install profile links to override environment-modules
ln -s %{_datadir}/lmod/lmod/init/profile %{buildroot}%{_sysconfdir}/profile.d/z00_lmod.sh
ln -s %{_datadir}/lmod/lmod/init/cshrc %{buildroot}%{_sysconfdir}/profile.d/z00_lmod.csh
%endif
# Install the rpm config file
install -Dpm 644 %{SOURCE1} %{buildroot}/%{macrosdir}/macros.%{name}
# TODO - contrib


%if 0%{?fedora} || 0%{?rhel} >= 8
%post
# Cleanup from pre-alternatives
[ ! -L %{_sysconfdir}/profile.d/modules.sh ] && rm -f %{_sysconfdir}/profile.d/modules.sh
%{_sbindir}/update-alternatives --install %{_sysconfdir}/profile.d/modules.sh modules.sh \
                                          %{_datadir}/lmod/lmod/init/profile 20 \
                                --slave %{_sysconfdir}/profile.d/modules.csh modules.csh \
                                        %{_datadir}/lmod/lmod/init/cshrc \
                                --slave %{_datadir}/fish/vendor_conf.d/modules.fish modules.fish \
                                        %{_datadir}/lmod/lmod/init/fish

%postun
if [ $1 -eq 0 ] ; then
  %{_sbindir}/update-alternatives --remove modules.sh %{_datadir}/lmod/lmod/init/profile
fi
%endif

%files
%license License
%doc INSTALL README.md README_lua_modulefiles.txt
%{_sysconfdir}/modulefiles
%config(noreplace) %{_sysconfdir}/profile.d/00-modulepath.csh
%config(noreplace) %{_sysconfdir}/profile.d/00-modulepath.sh
%if 0%{?fedora} || 0%{?rhel} >= 8
%ghost %{_sysconfdir}/profile.d/modules.csh
%ghost %{_sysconfdir}/profile.d/modules.sh
%dir %{_datadir}/fish/vendor_conf.d
%ghost %{_datadir}/fish/vendor_conf.d/modules.fish
%else
%{_sysconfdir}/profile.d/z00_lmod.csh
%{_sysconfdir}/profile.d/z00_lmod.sh
%endif
%{_datadir}/lmod
%{_datadir}/modulefiles
%{macrosdir}/macros.%{name}


%changelog
%autochangelog
