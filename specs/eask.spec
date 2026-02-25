%global npm_scope emacs-eask
%global npm_name  cli

Name:           eask
Version:        0.12.9
Release:        %{autorelease}
Summary:        Emacs Lisp dependency manager
License:        BlueOak-1.0.0 AND GPL-3.0-or-later AND ISC AND MIT
URL:            https://github.com/emacs-eask/cli
Source0:        https://registry.npmjs.org/@%{npm_scope}/%{npm_name}/-/%{npm_name}-%{version}.tgz

# nodejs-packaging-bundler @emacs-eask/cli && mv ~/rpmbuild/SOURCES/@emacs-eask-cli-* .
Source1:        @%{npm_scope}-%{npm_name}-%{version}-nm-prod.tgz
Source3:        @%{npm_scope}-%{npm_name}-%{version}-bundled-licenses.txt

BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch
BuildRequires:  /usr/bin/dos2unix
BuildRequires:  /usr/bin/jq
BuildRequires:  /usr/bin/node
BuildRequires:  /usr/bin/perl
BuildRequires:  nodejs-devel

Requires:       nodejs
Recommends:     emacs(bin)


%description
CLI for building, running, testing, and managing your Emacs Lisp dependencies.


%prep
%autosetup -n package

cp %{SOURCE3} .

# Set up bundled runtime (prod) node modules
tar xfz %{SOURCE1}
mkdir -p node_modules
pushd node_modules
ln -s ../node_modules_prod/* .
ln -s ../node_modules_prod/.bin .
popd

dos2unix --keepdate LICENSE
find -name \*.md -exec dos2unix --keepdate {} \+


%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{name}
cp -pr package.json cmds lisp src %{buildroot}%{nodejs_sitelib}/%{name}/

# Copy over bundled nodejs modules
cp -pr node_modules node_modules_prod %{buildroot}%{nodejs_sitelib}/%{name}/

install -p -D -m0755 %{name}.js %{buildroot}%{nodejs_sitelib}/%{name}/%{name}.js
mkdir -p %{buildroot}%{_bindir}
ln -sr %{buildroot}%{nodejs_sitelib}/%{name}/%{name}.js \
   %{buildroot}%{_bindir}/%{name}

# Sift licences from non-licences, etc.:
find %{buildroot}%{nodejs_sitelib}/%{name} \
     -type d -printf '%%%%dir %{nodejs_sitelib}/%{name}/%%P\0' \
     -o -name 'LICENSE*' -printf '%%%%license %{nodejs_sitelib}/%{name}/%%P\0' \
     -o -name '*.md' -printf '%%%%doc %{nodejs_sitelib}/%{name}/%%P\0' \
     -o -printf '%{nodejs_sitelib}/%{name}/%%P\0' \
    | perl -lp0e '
           my $directive = q();
           $directive = $1 if s/^(%%\w+ )//;
           s/%%/%%%%/g;
           s/([\"\\])/\\$1/g;
           $_ = $directive. qq("$_");
      ' \
      >filelist


%check
%{buildroot}%{_bindir}/%{name} --version

jq --arg spec_license '%{license}' \
   --exit-status \
   --slurp \
   '$spec_license == join(" AND ")' \
   @%{npm_scope}-%{npm_name}-%{version}-bundled-licenses.txt \
   >/dev/null


%files -f filelist
%doc README.md
%license @%{npm_scope}-%{npm_name}-%{version}-bundled-licenses.txt
%license LICENSE
%{_bindir}/%{name}


%changelog
%{autochangelog}
