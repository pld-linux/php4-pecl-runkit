%define		_modname	runkit
%define		_status		beta

Summary:	%{_modname} - mangle with user defined functions and classes
Summary(pl):	%{_modname} - obróbka zdefiniowanych przez u¿ytkownika funkcji i klas
Name:		php4-pecl-%{_modname}
Version:	0.4
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	05a690f04b7d2c42193f3e0c1bb99a19
URL:		http://pecl.php.net/package/runkit/
BuildRequires:	libtool
BuildRequires:	php4-devel >= 3:4.3.0
Requires:	php4-common >= 3:4.3.0
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php4
%define		extensionsdir	%{_libdir}/php4

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
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php4-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php4-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/README
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
