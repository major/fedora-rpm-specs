# This package is different from most node packages in Fedora because
# CoffeeScript is written in itself, and per Fedora policy we need to compile
# it--we can't ship the precompiled version.

%global commit f26d33d418dcdcfcc6ad3ab774d9cabbf7af659c
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           coffee-script
Version:        1.10.0
Release:        19%{?dist}
Summary:        A programming language that transcompiles to JavaScript
License:        MIT
URL:            http://coffeescript.org/
Source0:        https://github.com/jashkenas/%{name}/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

# some fixes for Cakefile, including:
#  - follow FHS and Fedora Node.js packaging guidelines
#  - support DESTDIR
#  - preserve timestamps when installing
Patch1:         %{name}-Cakefile.patch

# Fix 'basic exception throwing' test error.
# https://github.com/jashkenas/coffeescript/pull/5028
Patch2:	        coffee-script-2.3.0-Fix-a-test-relied-on-faulty-behavior.patch
# Fix Node.js 10+ compatibility due to: `[DEP0013] DeprecationWarning: Calling
# an asynchronous function without callback is deprecated.`
# https://github.com/jashkenas/coffeescript/pull/4340
Patch3:         coffee-script-1.12.0-Call-synchronous-fs-methods-using-the-Sync-variants.patch

Requires:       js-%{name} == %{version}-%{release}

BuildRequires:  nodejs-packaging
BuildRequires:  web-assets-devel
BuildRequires:  npm(underscore)
BuildRequires:  npm(uglify-js)

%description
CoffeeScript is a little language that compiles into JavaScript. Underneath all
of those embarrassing braces and semicolons, JavaScript has always had a
gorgeous object model at its heart. CoffeeScript is an attempt to expose the
good parts of JavaScript in a simple way.

The golden rule of CoffeeScript is: "It's just JavaScript". The code compiles
one-to-one into the equivalent JS, and there is no interpretation at runtime.
You can use any existing JavaScript library seamlessly (and vice-versa). The
compiled output is readable and pretty-printed, passes through JavaScript Lint
without warnings, will work in every JavaScript implementation, and tends to run
as fast or faster than the equivalent handwritten JavaScript.


%package -n js-%{name}
Summary:        A programming that transcompiles to JavaScript - core compiler

Provides:       %{name}-common = %{version}-%{release}
Obsoletes:      %{name}-common < 1.10.0-4

Requires:       web-assets-filesystem

%description -n js-%{name}
This is the core compiler for the CoffeeScript language, suitable for use in
browsers or by other JavaScript implementations.

For the primary compiler and cake utility used in conjunction with Node.js,
install the 'coffee-script' package.


%package doc
Summary:        A programming language that transcompiles to JavaScript - documentation

%description doc
The documentation for the CoffeeScript programming language.


%prep
%setup -qn coffeescript-%{commit}
%patch1 -p1
%patch2 -p1
%patch3 -p1

# Fix UglifyJS 3.x compatibility.
%nodejs_fixdep --dev uglify-js
sed -i '/uglify-js/ s/, fromString.*//' Cakefile

#rename documentation directory to html cause that's what we want in %%doc
mv documentation html


%build
%nodejs_symlink_deps --build
./bin/cake build

#build the minified coffee-script browser version and put it in its place
./bin/cake build:browser
mv extras/coffee-script.js extras/coffee-script.min.js

#also build the unminifed version
MINIFY=false ./bin/cake build:browser


%install
mkdir -p %{buildroot}%{_jsdir}/%{name}/
cp -pr extras/* %{buildroot}%{_jsdir}/%{name}/

mkdir -p %{buildroot}%{_datadir}/%{name}/extras/
ln -s %{_jsdir}/%{name}/coffee-script.js %{buildroot}%{_datadir}/%{name}/extras/
ln -s %{_jsdir}/%{name}/coffee-script.min.js %{buildroot}%{_datadir}/%{name}/extras/

mkdir -p %{buildroot}%{nodejs_sitelib}/%{name}
cp -pr *.js bin lib package.json %{buildroot}%{nodejs_sitelib}/%{name}
chmod 0644 %{buildroot}%{nodejs_sitelib}/%{name}/lib/coffee-script/parser.js
ln -sf %{_datadir}/%{name}/extras %{buildroot}%{nodejs_sitelib}/%{name}/extras

mkdir -p %{buildroot}%{_bindir}
ln -sf ../lib/node_modules/%{name}/bin/coffee %{buildroot}%{_bindir}/coffee
ln -sf ../lib/node_modules/%{name}/bin/cake %{buildroot}%{_bindir}/cake

#we skip %%nodejs_symlink_deps because this package has no dependencies, and if
#it did, would need special treatment anyway


%check
./bin/cake test


%pretrans -p <lua>
path = "%{nodejs_sitelib}/%{name}/lib"
st = posix.stat(path)
if st and st.type == "link" then
  os.remove(path)
end


%files
%{nodejs_sitelib}/%{name}
%{_bindir}/coffee
%{_bindir}/cake


%files -n js-%{name}
%doc README.md
%license LICENSE
%{_jsdir}/%{name}
%{_datadir}/%{name}


%files doc
%doc html


%changelog
* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 18 2021 Vít Ondruch <vondruch@redhat.com> - 1.10.0-16
- Fix FTBFS and some recent Node.js compatibility issues.
  Resolves: rhbz#1923684

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Tom Hughes <tom@compton.nu> - 1.10.0-5
- cleanup spec file, removing %%defattr

* Sat Nov 14 2015 Tom Hughes <tom@compton.nu> - 1.10.0-4
- update to comply with javascript packaging guidelines

* Fri Nov 13 2015 Tom Hughes <tom@compton.nu> - 1.10.0-3
- add temporary workaround for finding command line client

* Fri Nov 13 2015 Tom Hughes <tom@compton.nu> - 1.10.0-2
- fix resolution of path to command line client

* Sun Nov  8 2015 Tom Hughes <tom@compton.nu> - 1.10.0-1
- new upstream release 1.10.0
- enabled minified version now we have uglify-js

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 19 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.6.3-1
- new upstream release 1.6.3
  http://coffeescript.org/#changelog
- restrict architectures to ones that node works on

* Sun Feb 10 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.4.0-4
- fix rpmlint warnings
- rename documentation subpackage to "coffee-script-doc"

* Fri Feb 01 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.4.0-3
- rearrange symlinks to dep/provides generation works
- conditionalize minification so it works in the absence of uglify-js

* Thu Jan 31 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.4.0-2
- provide a -common subpackage with stuff useful for other JS runtimes/browsers
- split off the docs too

* Tue Jan 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.4.0-1
- new upstream release 1.4.0
- clean up for submission

* Sat Aug 20 2011 T.C. Hollingsworth <tchollingsworth@gmail.com> - 1.1.2-1
- initial package
