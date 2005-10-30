%define		_modname	runkit
%define		_status		beta
%define		_sysconfdir	/etc/php4
%define		extensionsdir	%{_libdir}/php4

Summary:	%{_modname} - mangle with user defined functions and classes
Summary(pl):	%{_modname} - obróbka zdefiniowanych przez u¿ytkownika funkcji i klas
Name:		php4-pecl-%{_modname}
Version:	0.4
Release:	4
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	05a690f04b7d2c42193f3e0c1bb99a19
URL:		http://pecl.php.net/package/runkit/
BuildRequires:	php4-devel >= 3:4.3.0
BuildRequires:	rpmbuild(macros) >= 1.254
%{?requires_php_extension}
Requires:	%{_sysconfdir}/conf.d
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Replace, rename, and remove user defined functions and classes. Define
customized superglobal variables for general purpose use. Execute code
in restricted environment (sandboxing).

In PECL status of this extension is: %{_status}.

%description -l pl
Zastêpowanie, zmiana nazwy lub usuwanie zdefiniowanych przez
u¿ytkownika funkcji i klas. Definiowanie zmiennych superglobalnych do
ogólnego u¿ytku. Wykonywanie danego kodu w ograniczonym ¶rodowisku
(sandbox).

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/conf.d,%{extensionsdir}}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}
cat <<'EOF' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -f /etc/apache/conf.d/??_mod_php4.conf ] || %service -q apache restart
[ ! -f /etc/httpd/httpd.conf/??_mod_php4.conf ] || %service -q httpd restart

%postun
if [ "$1" = 0 ]; then
	[ ! -f /etc/apache/conf.d/??_mod_php4.conf ] || %service -q apache restart
	[ ! -f /etc/httpd/httpd.conf/??_mod_php4.conf ] || %service -q httpd restart
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/%{_modname}.ini
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
